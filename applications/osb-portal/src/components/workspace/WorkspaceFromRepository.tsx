import * as React from "react";
import { makeStyles } from "@material-ui/core/styles";
import {
  Typography, Box, Button, Grid, CircularProgress
} from "@material-ui/core";

import { Repositories } from "../index";
import { WorkspaceEditor } from "./../index";
import RepositoryResourceBrowser from "../repository/RepositoryResourceBrowser";
import OSBChipList from "../common/OSBChipList";
import OSBPagination from "../common/OSBPagination";
import { OSBRepository, RepositoryResourceNode } from '../../apiclient/workspaces';
import RepositoryService from "../../service/RepositoryService";
import WorkspaceService from "../../service/WorkspaceService";
import { Workspace, OSBApplication } from "../../types/workspace";
import OSBDialog from "../common/OSBDialog";
import {
  fontColor,
  bgInputs,
  radius,
  bgLight,
  bgDarker,
} from "../../theme";
import Link from "@material-ui/core/Link";

export interface WorkspaceTemplate {
  title: string;
  application: OSBApplication;
}

export enum WorkspaceTemplateType {
  singleCell = 'singleCell',
  network = "network",
  explorer = "explorer",
  playground = "playground"
}


const useStyles = makeStyles((theme) => ({
  helperDialogText: {
    padding: `0px ${theme.spacing(1)}px ${theme.spacing(1)}px`,
    fontSize: '0.9rem',
  },
  info: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: theme.spacing(2),
    "& .MuiTypography-root": {
      paddingLeft: 0,
    },
  },
  repositoriesList: {
    "& .scrollbar": {
      borderBottomRightRadius: radius,
      borderBottomLeftRadius: radius,
    },
    "& .MuiBox-root": {
      maxHeight: '500px',
      marginRight: theme.spacing(2),
      marginLeft: theme.spacing(2),
      marginTop: theme.spacing(0),
      "& .MuiGrid-container": {
        backgroundColor: bgLight,
        "& .col": {
          paddingTop: 0,
          paddingBottom: 0,
          marginTop: 0,
          marginBottom: 0,
          "& .tag": {
            marginTop: 0,
            marginBottom: 0,
          },
        },
        "&:hover": {
          backgroundColor: bgDarker,
        },
      },
    },
  },
  resourceBrowser: {
    overflow: 'hidden',
    borderRadius: radius,
    backgroundColor: bgLight,
    margin: theme.spacing(2),
    "& .scrollbar": {
      overflow: 'auto',
      maxHeight: '400px',
      "& .MuiList-root": {
        paddingRight: '1rem',
        marginTop: 0,
        "& .MuiListItem-root": {
          alignItems: 'baseline',
        },
        "& p": {
          fontSize: '0.8rem',
          color: fontColor,
          "& span": {
            fontSize: '0.8rem',
            color: bgInputs,
          },
          "& .icon": {
            width: '2rem',
            display: 'flex',
            "& .MuiSvgIcon-root": {
              height: '1rem',
            },
          },
        },
      },
      "&::-webkit-scrollbar-thumb": {
        backgroundColor: bgInputs,
      },
      "&::-webkit-scrollbar-track": {
        backgroundColor: 'transparent',
      },
    },
    "& .flex-grow-1": {
      width: '100%',
    },
    "& .MuiTextField-root": {
      width: '96%',
      marginRight: '2%',
      marginLeft: '2%',
      padding: '0.6rem',
    },
  },
}))


export const WorkspaceFromRepository = ({ close, workspaceCreatedCallback }: { close: () => any, workspaceCreatedCallback: (refresh?: boolean, workspace?: Workspace) => void }) => {
  const [checked, setChecked] = React.useState<RepositoryResourceNode[]>([]);


  const classes = useStyles();
  const [selectedRepository, setSelectedRepository] = React.useState(null);

  enum Stage {
    SELECT_REPO,
    SELECT_FILES,
    EDIT_WORKSPACE,
    ERROR_NO_FILES
  }
  const [stage, setStage] = React.useState(Stage.SELECT_REPO);


  const handleBackAction = () => {
    if (stage > Stage.SELECT_REPO) {
      setStage(stage - 1);
      setChecked([]);
    }

  }

  const handleContinue = () => {
    if (stage < Stage.ERROR_NO_FILES)
      setStage(stage + 1)
  }

  const defaultWorkspace: Workspace = {
    resources: [],
    volume: null,
    shareType: null,
    name: "",
    description: null
  }

  const handleChipDelete = (key: string) => {
    const checkedChips = checked.filter(item => item.resource.path !== key);
    setChecked(checkedChips);
  }


  const onWorkspaceCreated = (refresh = false, ws: Workspace) => {
    document.getElementById("your-all-workspaces-tab").click(); // TODO replace with redux action
    if (checked.length > 0) {
      WorkspaceService.importResourcesToWorkspace(ws.id, checked.map(c => c.resource)).then(() => {
        setChecked([]);
        workspaceCreatedCallback(refresh, ws);
      });
    } else {
      workspaceCreatedCallback(refresh, ws);
    }
  }

  const SelectFilesFromRepository = ({ repositoryId }: any) => {
    let checkedIn: RepositoryResourceNode[] = [];
    const [repository, setRepository] = React.useState<OSBRepository>(null);
    React.useEffect(() => {
      RepositoryService.getRepository(repositoryId).then((repo) => {
        setRepository(repo);
      });
    }, []);
    const setCheckedArray = (newChecked: RepositoryResourceNode[]) => {
      checkedIn = newChecked
    }
    return repository ? <>
      <Box className={classes.resourceBrowser}>
        <RepositoryResourceBrowser repository={repository} checkedChanged={setCheckedArray} backAction={handleBackAction} />
      </Box>
      <Grid container={true} className={classes.info}>
        <Grid item={true}>
          <Typography component="h6" className={classes.helperDialogText}>
            Please select the files to add to your new workspace
          </Typography>
        </Grid>
        <Grid item={true}>
          <Button variant="contained" onClick={
            () => {
              handleContinue();
              setChecked(checkedIn);
            }
          }>Continue</Button>
        </Grid>
      </Grid>
    </> : <CircularProgress size={40}
      style={{
        position: 'relative',
        left: '45%',
        margin: '10px',
      }}
    />
  }

  const SelectRepository = () => {
    const [repositories, setRepositories] = React.useState<OSBRepository[]>(null);
    const [page, setPage] = React.useState(1);
    const [totalPages, setTotalPages] = React.useState(0);
    const [filter, setFilter] = React.useState("");

    const handlePageChange = (event: React.ChangeEvent<unknown>, pageNumber: number) => {
      setPage(pageNumber);
    }
    React.useEffect(() => {

      RepositoryService.getRepositoriesDetails(page).then((reposDetails) => {
        setRepositories(reposDetails.osbrepositories);
        setTotalPages(reposDetails.pagination.numberOfPages);
      });

    }, []);

    React.useEffect(() => {


      if (page !== 1) {
        setPage(1);
      } else {
        RepositoryService.getRepositoriesByFilter(page, { text: filter }).then((repos) => {
          setRepositories(repos.osbrepositories);
          setTotalPages(repos.pagination.numberOfPages);
        });
      }

    }, [filter]);

    React.useEffect(() => {

      RepositoryService.getRepositoriesByFilter(page, { text: filter }).then((repos) => {
        setRepositories(repos.osbrepositories);
        setTotalPages(repos.pagination.numberOfPages);
      });
    }, [page]);

    return repositories ? <>
      <Box className={classes.repositoriesList}>
        <Repositories repositories={repositories} handleRepositoryClick={(repositoryId) => {
          setSelectedRepository(repositoryId);
          setStage(Stage.SELECT_FILES);
        }
        } showSimpleVersion={true}
          searchRepositories={true} filterChanged={setFilter} />
        {totalPages > 1 ? <OSBPagination page={page} totalPages={totalPages} handlePageChange={handlePageChange} color="primary" showFirstButton={true} showLastButton={true} /> :
          null
        }
        <Grid container={true} className={classes.info}>
          <Grid item={true}>
            <Typography component="h6" className={classes.helperDialogText}>
              If you can't find what you're looking for, go <Link href="/repositories">here</Link> to explore
              all the OSB repositories, or add a new one.
            </Typography>
          </Grid>
        </Grid>
      </Box>
    </> : <CircularProgress size={40}
      style={{
        position: 'relative',
        left: '45%',
        margin: '10px',
      }}
    />
  }

  const handleClose = () => {
    setStage(Stage.SELECT_REPO);
    close();
  }

  const returnDialoged = (children: any) => {
      return (
        <OSBDialog
          title="Create new workspace"
          open={true}
          closeAction={handleClose}
          maxWidth="md">
          {children}
        </OSBDialog>
    )
  }


  switch (stage) {
    case Stage.SELECT_REPO:
      return (
         returnDialoged(<SelectRepository />)
    )
    case Stage.SELECT_FILES:
      return (
        returnDialoged(<SelectFilesFromRepository repositoryId={selectedRepository} />)
    )
    case Stage.EDIT_WORKSPACE:
      return <>
        <WorkspaceEditor title={"Create new workspace"} open={true} workspace={defaultWorkspace} onLoadWorkspace={onWorkspaceCreated} closeHandler={handleClose} >
        {checked.length > 0 && <OSBChipList chipItems={checked} onDeleteChip={(chipPath: string) => handleChipDelete(chipPath)} />}
      </WorkspaceEditor>
      </>
    case Stage.ERROR_NO_FILES:
      return (
        returnDialoged(
          <Grid container={true} className={classes.info}>
            <Grid item={true}>
              <Typography component="h6" className={classes.helperDialogText}>
                No files from this repository have been selected, and so all the files in the repository will be added in the workspace. Press OK to proceed, or press Cancel and go back and select some.
              </Typography>
            </Grid>
            <Grid item={true}>
              <Button color="primary" onClick={() => setStage(Stage.SELECT_FILES)}>Cancel</Button>
              <Button variant="contained" color="primary" onClick={() => setStage(Stage.EDIT_WORKSPACE)}>OK</Button>
            </Grid>
          </Grid>
        )
    )
    default:
      return null
  }
}

export default WorkspaceFromRepository;
