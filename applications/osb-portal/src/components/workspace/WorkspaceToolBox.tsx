import * as React from 'react';

import { makeStyles } from '@material-ui/core/styles';
import { Typography, Grid, Paper } from '@material-ui/core';
import RadioButtonUncheckedIcon from '@material-ui/icons/RadioButtonUnchecked';
import Button from '@material-ui/core/Button';
import AppsOutlinedIcon from '@material-ui/icons/AppsOutlined';
import InsertChartOutlinedIcon from '@material-ui/icons/InsertChartOutlined';
import CodeOutlinedIcon from '@material-ui/icons/CodeOutlined';

import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText, { DialogContentTextTypeMap } from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import IconButton from '@material-ui/core/IconButton';
import SvgIcon from '@material-ui/core/SvgIcon';
import TextField from '@material-ui/core/TextField';

import { UserInfo } from '../../types/user';

import * as workspaceApi from '../../apiclient/workspaces/apis';
import { WorkspacePostRequest } from '../../apiclient/workspaces/apis/RestApi';
import * as modelWorkspace from '../../apiclient/workspaces/models/Workspace';
import { Configuration } from '../../apiclient/workspaces';

const useStyles = makeStyles((theme) => ({
  paper: {
    padding: theme.spacing(2),
    paddingBottom: theme.spacing(4),
    margin: theme.spacing(1),
    textAlign: 'center',
  },
  iconButton: {
    width: 24,
    height: 24,
    marginTop: 4,
    padding: 0,
    float: 'right',
  },
  svgIcon: {
    paddingTop: 6,
    paddingLeft: 4,
  },
  dialogContent: {
    paddingBottom: 16,
  },
  dialogContentText: {
    width: '50%',
  },
  dialogTextField: {
    width: '80%',
  },
  dialogButtons: {
    position: 'absolute',
    bottom: 16,
    right: 16,
  },
  roundedButton: {
    borderRadius: '5em',
    borderWidth: '2px',
    borderColor: theme.palette.text.primary,
    borderStyle: 'solid',
    paddingTop: theme.spacing(1),
    paddingBottom: theme.spacing(1),
    minWidth: theme.spacing(15),
    textTransform: 'inherit',
  },
  roundedButtonActive: {
    borderRadius: '5em',
    borderWidth: '2px',
    borderColor: theme.palette.text.primary,
    background: theme.palette.text.primary,
    color: theme.palette.background.paper,
    borderStyle: 'solid',
    paddingTop: theme.spacing(1),
    paddingBottom: theme.spacing(1),
    minWidth: theme.spacing(15),
    textTransform: 'inherit',
    '&:hover': {
      color: theme.palette.text.primary,
    },
  },
  h3: {
    marginBottom: theme.spacing(6),
  }
}));

export const WorkspaceToolBox = (props: any) => {
  const classes = useStyles();

  const user: UserInfo = props.user;
  const keycloak = props.keycloak;

  let newWorkspaceInput: { value: string; } = null;
  let type: string = props.type;

  const [show, setShow] = React.useState(false);
  const handleClickOpen = () => {
    setShow(true);
  };
  const handleClose = () => {
    setShow(false);
  };

  const handleUserLogin = () => {
    keycloak.login();
  }
  const handleSignup = () => {
    keycloak.register();
  }

  const createSingleCell = () => {
    type = '1';
    handleClickOpen();
  }

  const inputRefNew = (el: any) => newWorkspaceInput = el;

  const handleCreateWorkspace = async () => {
    const newWorkspace: modelWorkspace.Workspace = {name: newWorkspaceInput.value, description: ''};

    keycloak.updateToken(1);
    const api = new workspaceApi.RestApi(new Configuration({basePath: '/api/workspaces/api/', accessToken: keycloak.token}));
    const wspr: WorkspacePostRequest = {workspace: newWorkspace};
    const result = await api.workspacePost(wspr).then(workspace => {
      if (workspace && workspace.id) {
        // ToDo: if not workspace or no id raise an error
        props.onLoadWorkspaces();
        handleClose();
      };
    });
  }

  let dialogContent = null;
  if (user === undefined || user === null) {
    dialogContent = <>
    <DialogContentText id="new-worspace-in-dialog-text" className={classes.dialogContentText}>
      To create a new workspace you need a Open Source Brain account. If you already have one please sign in, if not create one for free. Workspaces will let you save your own models and data, run simulations and analysis.
    </DialogContentText>
    <DialogActions className={classes.dialogButtons}>
      <Button onClick={handleSignup} className={classes.roundedButton}>
          Sign Up
      </Button>
      <Button onClick={handleUserLogin} autoFocus={true} className={classes.roundedButtonActive}>
          Sign In
      </Button>
    </DialogActions>
    </>
  } else {
    dialogContent = <>
    <TextField id='standard-basic' label='Name of the workspace' fullWidth={true} className={classes.dialogTextField} inputRef={inputRefNew}  />
    <DialogActions className={classes.dialogButtons}>
      <Button onClick={handleCreateWorkspace} className={classes.roundedButton}>
          Create
      </Button>
    </DialogActions>
    </>
  }

  return (
    <>
    <Dialog onClose={handleClose} open={show} maxWidth={'md'} fullWidth={true}>
      <DialogTitle id="new-workspace-dialog-title">
        {"Create a new workspace"}
        <IconButton aria-label="close" className={classes.iconButton} onClick={handleClose}>
          <SvgIcon  className={classes.svgIcon}>
            <path d="M12 4.5L4 12.5" stroke={'white'} strokeWidth={2} strokeLinecap={'round'} strokeLinejoin={'round'}/>
            <path d="M4 4.5L12 12.5" stroke={'white'} strokeWidth={2} strokeLinecap={'round'} strokeLinejoin={'round'}/>
          </SvgIcon>
        </IconButton>
      </DialogTitle>
      <DialogContent className={classes.dialogContent}>
        {dialogContent}
      </DialogContent>
    </Dialog>
    <Paper className={classes.paper}>
    <h3 className={classes.h3}>Create a new Workspace</h3>
      <Grid container={true}>
        <Grid item={true} xs={3} onClick={createSingleCell}>
          <RadioButtonUncheckedIcon fontSize="large"/>
          <Typography variant="subtitle1">Single Cell</Typography>
          <Typography variant="caption">NetPyNe</Typography>
        </Grid>
        <Grid item={true} xs={3}>
          <AppsOutlinedIcon fontSize="large" />
          <Typography variant="subtitle1">Network</Typography>
          <Typography variant="caption">NetPyNe</Typography>
        </Grid>
        <Grid item={true} xs={3}>
          <InsertChartOutlinedIcon fontSize="large" />
          <Typography variant="subtitle1">Data Analyses</Typography>
          <Typography variant="caption">NWB Explorer</Typography>
        </Grid>
        <Grid item={true} xs={3}>
          <CodeOutlinedIcon fontSize="large" />
          <Typography variant="subtitle1">Playground</Typography>
          <Typography variant="caption">Jupyter Lab</Typography>
        </Grid>
      </Grid>
    </Paper>
    </>
  )
}