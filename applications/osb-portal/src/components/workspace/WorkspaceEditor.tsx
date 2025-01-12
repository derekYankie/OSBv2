import * as React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import Box from "@material-ui/core/Box";
import Grid from "@material-ui/core/Grid";
import IconButton from "@material-ui/core/IconButton";
import Typography from '@material-ui/core/Typography';
import CircularProgress from '@material-ui/core/CircularProgress'
import Dialog from "@material-ui/core/Dialog";
import DialogTitle from "@material-ui/core/DialogTitle";
import DialogContent from "@material-ui/core/DialogContent";
import DialogActions from "@material-ui/core/DialogActions";
import Dropzone from 'react-dropzone'
import DeleteForeverIcon from '@material-ui/icons/DeleteForever';
import { fade } from '@material-ui/core/styles/colorManipulator';
import { Autocomplete } from "@material-ui/lab";
import MDEditor from 'react-markdown-editor-lite';
// import style manually
import 'react-markdown-editor-lite/lib/index.css';
import MarkdownViewer from "../common/MarkdownViewer";
import Chip from "@material-ui/core/Chip";

import { Workspace } from '../../types/workspace';
import { Tag } from "../../apiclient/workspaces";
import WorkspaceService from "../../service/WorkspaceService";
import OSBDialog from "../common/OSBDialog";

import {
  bgLight,
  radius, gutter,
  bgInputs,
} from "../../theme";

const useStyles = makeStyles((theme) => ({
  actionButton: {
    marginLeft: theme.spacing(2),
  },
  actionBox: {
    backgroundColor: bgLight,
  },
  outerBox: {
    marginTop: 0
  },
  dropZoneBox: {
    color: bgInputs,
    border: `2px dashed ${bgInputs}`,
    borderRadius: 5,
    padding: 4,
    "& .MuiTypography-subtitle2": {
      marginTop: theme.spacing(1),
      marginBottom: theme.spacing(2),
    },
    "& .MuiButton-outlined": {
      margin: '0 auto',
      display: 'flex',
      justifyContent: 'center',
      color: bgInputs,
      borderRadius: radius,
      border: `2px solid ${bgInputs}`,
    },
  },
  imagePreview: {
    display: 'flex', minHeight: "15em", alignItems: 'stretch', backgroundPosition: "center", backgroundSize: 'cover', flex: 1
  },
  autocomplete: {
    marginTop: theme.spacing(1),
    '& .MuiChip-root': {
      backgroundColor: bgLight,
    }
  },
}));

const MAX_ALLOWED_THUMBNAIL_SIZE = 1024 * 1024; // 1MB

interface WorkspaceEditProps {
  workspace: Workspace;
  onLoadWorkspace: (refresh?: boolean, workspace?: Workspace) => void;
  closeHandler?: () => void;
  filesSelected?: boolean;
  tags: Tag[];
  retrieveAllTags?: (page: number) => void;
  children?: any;
  title: string;
  open: boolean;

}

const dropAreaStyle = (error: any) => ({
  flex: 1,
  display: 'flex',
  alignItems: 'center',

  borderRadius: radius,
  padding: gutter,
  borderColor: error ? "red" : fade(bgInputs, 1),
});

async function readFile(file: Blob) {
  return new Promise((resolve, reject) => {
    const fileReader: FileReader = new FileReader();

    fileReader.onload = () => {
      resolve(fileReader.result);
    };

    fileReader.onerror = reject;

    fileReader.readAsArrayBuffer(file);
  })
}

let thumbnail: Blob;

export default (props: WorkspaceEditProps) => {

  const classes = useStyles();

  const { workspace } = props;
  const [workspaceForm, setWorkspaceForm] = React.useState<
    Workspace
  >({ ...props.workspace });

  const closeWorkSpaceEditor = () => {
    if (props.closeHandler) {
      props.closeHandler();
    }
  }

  const [thumbnailPreview, setThumbnailPreview] = React.useState<any>(workspace?.thumbnail ? "/proxy/workspaces/" + workspace.thumbnail : null);
  const [thumbnailError, setThumbnailError] = React.useState<any>(null);
  const [showNoFilesSelectedDialog, setShowNoFilesSelectedDialog] = React.useState(false);
  const workspaceTags = workspace && workspace.tags ? workspace.tags.map((tagObject) => tagObject.tag) : [];
  const [defaultTags, setDefaultTags] = React.useState(workspaceTags);

  const handleCreateWorkspaceButtonClick = () => {
    if (typeof props.filesSelected !== 'undefined') {
      props.filesSelected ? handleCreateWorkspace() :
        setShowNoFilesSelectedDialog(!showNoFilesSelectedDialog);
    }
    else {
      handleCreateWorkspace();
    }
  }

  const handleCreateWorkspace = async () => {
    setLoading(true);
    WorkspaceService.createOrUpdateWorkspace({ ...workspace, ...workspaceForm }).then(
      async (returnedWorkspace) => {
        props.retrieveAllTags(1);
        if (thumbnail && !thumbnailError) {
          const fileThumbnail: any = await readFile(thumbnail);
          WorkspaceService.updateWorkspaceThumbnail(returnedWorkspace.id, new Blob([fileThumbnail]))
            .then(() => props.onLoadWorkspace(true, returnedWorkspace),
              e => console.error('Error uploading thumbnail', e)
            );
        } else {
          setLoading(true)
          props.onLoadWorkspace(true, returnedWorkspace)
        }
      }
      , (e) => {
        setLoading(false);
        throw new Error('Error submitting the workspace')
        // console.error('Error submitting the workspace', e);
      }

    );

  }



  const previewFile = (file: Blob) => {
    if (!file) {
      setThumbnailError(null);
      setThumbnailPreview(null);
      return;
    }

    if (!file.type.includes("image")) {
      setThumbnailError("Not an image file");
      return;
    }
    if (file.size > MAX_ALLOWED_THUMBNAIL_SIZE) {
      setThumbnailError("File exceeds allowed size (1MB)");
      return;
    }

    setThumbnailError(null)

    const fileReader: FileReader = new FileReader();

    fileReader.onload = () => {
      setThumbnailPreview(fileReader.result);
    };

    fileReader.readAsDataURL(file);

  }

  const setNameField = (e: any) =>
    setWorkspaceForm({ ...workspaceForm, name: e.target.value });
  const setDescriptionField = (e: any) =>
    setWorkspaceForm({ ...workspaceForm, description: e.text });
  const setThumbnail = (uploadedThumbnail: any) => {
    thumbnail = uploadedThumbnail;
    previewFile(thumbnail);
  }
  const setWorkspaceTags = (tagsArray: string[]) => {
    const arrayOfTags: Tag[] = [];
    tagsArray.forEach(tag => { arrayOfTags.push({ tag }); });
    setWorkspaceForm({ ...workspaceForm, tags: arrayOfTags });
  }
  const [loading, setLoading] = React.useState(false);

  return (
    <>

      <OSBDialog
        title={props.title}
        open={props.open}
        closeAction={closeWorkSpaceEditor}
        maxWidth="md"
        actions={
          <React.Fragment>
            <Button disabled={loading} color="primary" onClick={closeWorkSpaceEditor}>
              Cancel
            </Button>
            <Button className={classes.actionButton} variant="contained" color="primary" disabled={loading} onClick={handleCreateWorkspaceButtonClick}>
              {workspace.id ? "Save" : "Create A New Workspace"}
            </Button>
          </React.Fragment>
        }>
        <Box p={2} mt={4} className={classes.outerBox}>
          {props.children && <Box>{props.children}</Box>}
          <Box>
            <Typography component="label" variant="h6">
              Workspace name
            </Typography>
            <TextField
              id="workspaceName"
              placeholder="Name"
              fullWidth={true}
              onChange={setNameField}
              variant="outlined"
              defaultValue={props.workspace.name}
            />
          </Box>

          <Box mt={4} alignItems="stretch">
            <Typography component="label" variant="h6">
              Workspace tags
            </Typography>
            <Autocomplete
              multiple={true}
              freeSolo={true}
              className={classes.autocomplete}
              options={props.tags.map(tagObject => tagObject.tag)}
              defaultValue={defaultTags}
              onChange={(event, value) => setWorkspaceTags(value)}
              renderTags={(value, getTagProps) =>
                value.map((option, index) => (
                  <Chip variant="outlined" label={option} {...getTagProps({ index })} key={option} />
              ))
              }
              renderInput={(params) => (
                <TextField InputProps={{ disableUnderline: true }} fullWidth={true} {...params} variant="filled" />
              )}
            />
          </Box>

          <Box mt={4}>
            <Typography component="label" variant="h6">
              Workspace description
            </Typography>

            <MDEditor
              defaultValue={workspace?.description}
              onChange={setDescriptionField}
              view={{ html: false, menu: true, md: true }}
              renderHTML={(text: string) => <MarkdownViewer text={text} />}
            />

          </Box>
          <Box mt={4} alignItems="stretch" >
            <Typography component="label" variant="h6">
              Workspace thumbnail
            </Typography>
            <Box alignItems="stretch" className={classes.dropZoneBox}>
              <Dropzone onDrop={(acceptedFiles: any) => { setThumbnail(acceptedFiles[0]) }}>
                {({ getRootProps, getInputProps, acceptedFiles }: { getRootProps: (p: any) => any, getInputProps: () => any, acceptedFiles: any[] }) => (
                  <section className={classes.imagePreview} style={{ backgroundImage: !thumbnailError && `url(${thumbnailPreview})` }}>
                    <div {...getRootProps({ style: dropAreaStyle(thumbnailError) })}>
                      <input {...getInputProps()} />
                      <Grid container={true} justify="center" alignItems="center" direction="row">
                        {acceptedFiles.length !== 0 && <Grid item={true}>
                          {/* <IconButton><PublishIcon /></IconButton> */}
                          {acceptedFiles.length === 0 ? '' :
                            <IconButton
                              onClick={(e: any) => {
                                e.preventDefault();
                                setThumbnail(null)
                              }
                              }
                            >
                              <DeleteForeverIcon />
                            </IconButton>}
                        </Grid>
                        }
                        <Grid item={true} >
                          <Box component="div" m={1} >
                            <Typography variant="subtitle2" component="p">
                              {acceptedFiles.length === 0 ?
                                "Drop file here to upload..."
                                :
                                  null
                              }
                            </Typography>
                            <Button variant="outlined">
                              Browse files
                            </Button>
                            {
                              thumbnailError &&
                                <Typography color="error" variant="subtitle2" component="p">
                                  {
                                    thumbnailError
                                  }
                                </Typography>
                            }
                          </Box>
                        </Grid>
                      </Grid>
                    </div>
                  </section>
                )}
              </Dropzone>
            </Box>
          </Box>
        </Box>
      </OSBDialog>
      {loading &&
        <Box mt={4} p={2} className={classes.actionBox} textAlign="right">
          <CircularProgress
            size={24}
            style={{
              position: 'absolute',
              top: '50%',
              left: '50%',
              marginTop: -12,
              marginLeft: -12,
            }}
          />
        </Box>
      }
      {
        showNoFilesSelectedDialog && <Dialog open={showNoFilesSelectedDialog}
          onClose={() => setShowNoFilesSelectedDialog(false)}>
          <DialogTitle>No files selected</DialogTitle>
          <DialogContent>{
            "No files from this repository have been selected, and so all the files in the repository will be added in the workspace. Press OK to proceed, or press Cancel and go back and select some."
          }</DialogContent>
          <DialogActions>
            <Button color="primary" onClick={() => setShowNoFilesSelectedDialog(false)}>Cancel</Button>
            <Button variant="contained" color="primary" onClick={() => { handleCreateWorkspace(); setShowNoFilesSelectedDialog(false) }} disabled={loading}>OK</Button>
          </DialogActions>
        </Dialog>
      }

    </>
  );
};
