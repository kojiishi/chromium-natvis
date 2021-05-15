# chromium-natvis

A local fork of [blink.natvis] for chromium.

[blink.natvis]: https://source.chromium.org/chromium/chromium/src/+/main:tools/win/DebugVisualizers/blink.natvis?q=natvis&ss=chromium%2Fchromium%2Fsrc

## Install

You can download the natvis file, or clone the repository,
and place it in one of the [natvis file locations].

If you want to save under your "Documents" directory,
be aware that your "Documents" directory is redirected,
to such as the one in OneDrive.
PowerShell can find it by the following command:
```
PS> cd ([Environment]::GetFolderPath('MyDocuments'))
PS> cd "Visual Studio 2019"
PS> cd Visualizers
```

### Download

Downlaod `blink.natvis` from
[here](https://raw.githubusercontent.com/kojiishi/chromium-natvis/main/blink.natvis)
and save to one of the [natvis file locations].

### Clone

```
> cd ..
> ren Visualizers Visualizers.bak
> git clone https://github.com/kojiishi/chromium-natvis.git Visualizers
> move Visualizers.bak\* Visualizers
```

### Local vs PDB

Often _.natvis_ files built into PDB files win over your local files.
You [can't update _.natvis_ files that are embedded in .pdb files while you're
debugging](https://docs.microsoft.com/en-us/visualstudio/debugger/create-custom-views-of-native-objects?view=vs-2019#:~:text=You%20can%27t%20update%20.natvis%20files%20that%20are%20embedded%20in%20.pdb%20files%20while%20you%27re%20debugging.).

If you prefer to remove _.natvis_ files from PDB files,
you can comment out the _.natvis_ files in `BUILD.gn`.
See [DebugVisualizers/README].

If you change `BUILD.gn` in your repo,
you may also want to avoid checking in the change.
The following command can avoid checking in the changes to `BUILD.gn`.
```
> git update-index --skip-worktree tools/win/DebugVisualizers/BUILD.gn
```
Confirm it's skipped:
```
> git ls-files -v | grep ^S
```
When you want to revert it back to the original state:
```
> git update-index --no-skip-worktree tools/win/DebugVisualizers/BUILD.gn
```

You may prefer `--assume-unchanged` instead of `--skip-worktree`,
depending on your work style.

[DebugVisualizers/README]: https://source.chromium.org/chromium/chromium/src/+/main:tools/win/DebugVisualizers/README.md
[natvis file locations]: https://docs.microsoft.com/en-us/visualstudio/debugger/create-custom-views-of-native-objects?view=vs-2019#BKMK_natvis_location
