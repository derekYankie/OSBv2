import * as React from "react";
import { Typography, Box, ButtonBase, Button } from "@material-ui/core";

import { UserInfo } from "../../types/user";
import OSBDialog from "../common/OSBDialog";
import { NewWorkspaceAskUser } from "..";
import WorkspaceEdit from "./WorkspaceEditor";
import { Workspace, SampleResourceTypes, OSBApplication } from "../../types/workspace";

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

const WorkspaceTemplates: { [id: string]: Workspace } = {
  [WorkspaceTemplateType.singleCell]: {
    resources: [{
      name: "singleCellModel.np",
      type: SampleResourceTypes.m,
    }],
    volume: null,
    shareType: null,
    name: null,
    description: null
  },
  [WorkspaceTemplateType.network]: {
    resources: [{
      name: "networkModel.np",
      type: SampleResourceTypes.m,
    }],
    volume: null,
    shareType: null,
    name: null,
    description: null
  },
  [WorkspaceTemplateType.explorer]: {
    resources: [{
      name: "sampleNwbFile.nwb",
      type: SampleResourceTypes.e,
    }],
    volume: null,
    shareType: null,
    name: null,
    description: null
  },
  [WorkspaceTemplateType.playground]: {
    resources: [{
      name: "notebook.ipynb",
      type: SampleResourceTypes.g,
    }],
    volume: null,
    shareType: null,
    name: null,
    description: null
  }
}

interface ItemProps {
  icon: React.ElementType;
  title: string,
  template: WorkspaceTemplateType,
  user: UserInfo;
}

export default (props: ItemProps) => {
  const { user, template, title } = props;
  const [askLoginOpen, setAskLoginOpen] = React.useState(false);
  const [newWorkspaceOpen, setNewWorkspaceOpen] = React.useState(false);

  const handleClick = () => {
    if (!user) {
      setAskLoginOpen(true);
    } else {
      setNewWorkspaceOpen(true);
    }
  };

  const closeAskLogin = () => setAskLoginOpen(false);

  const closeNewWorkspace = () => {
    setNewWorkspaceOpen(false);
  }
  const defaultWorkspace: Workspace = WorkspaceTemplates[template];

  return (
    <>
      <Button style={{ textTransform: "none" }} onClick={handleClick}>
        <Box textAlign="center">
          <props.icon style={{ marginBottom: "0.2em" }} />
          <Typography variant="subtitle1">{title}</Typography>
          <Typography variant="caption">{defaultWorkspace.resources[0].type.application.name}</Typography>
        </Box>
      </Button>
      <OSBDialog
        title="Create new workspace"
        open={askLoginOpen}
        closeAction={closeAskLogin}
      >
        <NewWorkspaceAskUser />
      </OSBDialog>
      <OSBDialog
        title="Create new workspace"
        open={newWorkspaceOpen}
        closeAction={closeNewWorkspace}
      >
        <WorkspaceEdit workspace={defaultWorkspace} onLoadWorkspace={closeNewWorkspace} />
      </OSBDialog>
    </>
  );
};
