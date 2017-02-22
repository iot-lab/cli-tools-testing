import pytest

import subprocess

TOOLS = {
  "auth-cli":
     "",  # no subcommands
  "experiment-cli":
     "submit,stop,get,load,info,wait",
  "profile-cli":
     "addwsn430,addm3,adda8,addcustom,del,get,load",
  "node-cli":
     "",  # no subcommands
  "robot-cli":
     "status,update,get",
  "open-a8-cli":
     "wait-for-boot,reset-m3,flash-m3,run-script,run-cmd,copy-file",
}

@pytest.mark.parametrize("tool", TOOLS)
def test_cli_tools_no_args(tool):
    with pytest.raises(subprocess.CalledProcessError):
        run(tool)  # commands return 1 if no args given

@pytest.mark.parametrize("tool", TOOLS)
def test_cli_tools_help(tool):
    run(tool+" -h")

@pytest.mark.parametrize("tool, cmd", [ (tool, cmd)
    for tool in TOOLS for cmd in TOOLS[tool].split(",") ])
def test_command_help(tool, cmd):
    run(tool+" "+cmd+" -h")


def run(cmd):
    cmd = cmd.split()
    ret = subprocess.check_output(cmd)
    return ret
