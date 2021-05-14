# chromium-natvis

A local fork of [blink.natvis] for chromium.

[blink.natvis]: https://source.chromium.org/chromium/chromium/src/+/main:tools/win/DebugVisualizers/blink.natvis?q=natvis&ss=chromium%2Fchromium%2Fsrc

## Install

Install the `blink.natvis` to one of the [natvis file locations].

If you prefer to clone to under the "Documents" directory,
the "Documents" directory may be redirected,
such as to the "Documents" directory in OneDrive.
PowerShell can find the correct "Documents" directory.
```
PS> cd ([Environment]::GetFolderPath('MyDocuments'))
PS> cd "Visual Studio 2019"
PS> ren Visualizers Visualizers.bak
PS> git clone https://github.com/kojiishi/chromium-natvis.git Visualizers
PS> move Visualizers.bak\* Visualizers
```

Often `natvis` built into PDB files win over your local files.
To remove `natvis` from PDB files,
comment out the `natvis` files in `BUILD.gn`.
See [DebugVisualizers/README].

If you change `BUILD.gn` in your repo,
you can also do the following to avoid checking in the changes to `BUILD.gn`.
```
> git update-index --skip-worktree tools/win/DebugVisualizers/BUILD.gn
```
Confirm it's skipped:
```
> git ls-files -v | grep ^S
```
or revert back when you need:
```
> git update-index --no-skip-worktree tools/win/DebugVisualizers/BUILD.gn
```

You may prefer `--assume-unchanged` instead of `--skip-worktree`,
depending on your work style.

[DebugVisualizers/README]: https://source.chromium.org/chromium/chromium/src/+/main:tools/win/DebugVisualizers/README.md
[natvis file locations]: https://docs.microsoft.com/en-us/visualstudio/debugger/create-custom-views-of-native-objects?view=vs-2019#BKMK_natvis_location
