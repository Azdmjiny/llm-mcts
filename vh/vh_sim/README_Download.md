# VirtualHome Simulator

`vh_sim` is a local runtime dependency and is intentionally ignored by Git. It
contains the VirtualHome API, Unity executable, and large data files.

Download the API and the Linux x86-64 simulator from the
[official VirtualHome repository](https://github.com/xavierpuigf/virtualhome),
then place the API contents under this directory. The Unity executable and its
matching `_Data` directory must be placed in:

```
vh/vh_sim/simulation/unity_simulator/
```

The executable path is supplied through the project's command-line options;
use the exact filename downloaded for your platform. See the official
VirtualHome README for platform-specific setup and Unity runtime requirements.
