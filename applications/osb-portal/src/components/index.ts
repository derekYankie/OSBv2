import { connect } from 'react-redux'

import { App as app } from './App'
import { Workspaces as workspace } from './workspace/Workspaces'
import { Banner as banner } from './header/Banner'
import { Header as header } from './header/Header'
import { WorkspaceDrawer as workspacedrawer } from './drawer/WorkspaceDrawer'

import { RootState } from '../store/rootReducer'
import { fetchWorkspacesAction } from '../store/actions/workspaces'
import { fetchModelsAction } from '../store/actions/models';
import { fetchNWBFilesAction } from '../store/actions/nwbfiles';
import { userLogin, userLogout } from '../store/actions/user'
import { toggleDrawer } from '../store/actions/drawer'

const mapWorkspaceStateToProps = (state: RootState) => ({
  workspaces: state.workspaces,
});
const dispatchWorkspaceProps = {
  onLoadWorkspaces: fetchWorkspacesAction,
  onLoadModels: fetchModelsAction,
  onLoadNWBFiles: fetchNWBFilesAction
}

const mapUserStateToProps = (state: RootState) => ({
  user: state.user,
});
const dispatchUserProps = {
  onUserLogin: userLogin,
  onUserLogout: userLogout
}
const mapDrawerStateToProps = (state: RootState) => ({
  drawer: state.drawer,
});
const dispatchDrawerProps = {
  onToggleDrawer: toggleDrawer
}

export const Workspaces = connect(mapWorkspaceStateToProps, dispatchWorkspaceProps)(workspace)
export const Banner = connect(mapUserStateToProps)(banner)
export const Header = connect(mapUserStateToProps, {...dispatchUserProps, ...dispatchDrawerProps})(header)
export const WorkspaceDrawer = connect(mapDrawerStateToProps, dispatchDrawerProps)(workspacedrawer)
export const App = connect(mapWorkspaceStateToProps, dispatchWorkspaceProps)(app)