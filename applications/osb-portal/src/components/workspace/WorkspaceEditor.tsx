import * as React from "react";

import { makeStyles } from "@material-ui/core/styles";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import Box from "@material-ui/core/Box";
import Grid from "@material-ui/core/Grid";
import MarkdownIt from "markdown-it";
import MdEditor from "react-markdown-editor-lite";
import "react-markdown-editor-lite/lib/index.css";

import { workspacesApi } from "../../middleware/osbbackend";
import { WorkspacePostRequest } from "../../apiclient/workspaces/apis/RestApi";
import * as modelWorkspace from "../../apiclient/workspaces/models/Workspace";

interface WorkspaceEditProps {
  workspace: modelWorkspace.Workspace;
  onLoadWorkspace: (workspace: modelWorkspace.Workspace) => void;
}

export default (props: WorkspaceEditProps) => {
  const mdParser = new MarkdownIt(/* Markdown-it options */);
  const [workspaceForm, setWorkspaceForm] = React.useState<
    modelWorkspace.Workspace
  >({ ...props.workspace });

  const renderMarkdown = (text: string) => {
    return mdParser.render(text);
  };

  const handleCreateWorkspace = async () => {
    const newWorkspace: modelWorkspace.Workspace = workspaceForm;

    const wspr: WorkspacePostRequest = { workspace: newWorkspace };
    await workspacesApi.workspacePost(wspr).then((workspace) => {
      if (workspace && workspace.id) {
        // TODO: if not workspace or no id raise an error
        props.onLoadWorkspace(workspace);
      }
    });
  };

  const setNameField = (e: any) =>
    setWorkspaceForm({ ...workspaceForm, name: e.target.value });
  const setDescriptionField = (e: any) =>
    setWorkspaceForm({ ...workspaceForm, description: e.text });
  return (
    <>
      <Grid container={true} justify="flex-start" spacing={1}>
        <Grid item={true} xs={12}>
          <TextField
            id="standard-basic"
            label="Name of the workspace"
            fullWidth={true}
            onChange={setNameField}
          />
        </Grid>
        <Grid item={true} xs={12}>
          <MdEditor
            value={workspaceForm.description}
            style={{ height: "20vh" }}
            renderHTML={renderMarkdown}
            onChange={setDescriptionField}
          />
        </Grid>
        <Grid item={true} xs={12} direction="column" alignItems="flex-end">
          <Button variant="contained" onClick={handleCreateWorkspace}>
            Create
          </Button>
        </Grid>
      </Grid>
    </>
  );
};
