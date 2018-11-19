# Western
A project? I guess. will include 3GS 3.0 and 3.0.1 bundles in the future. A wrapper for OUTDATED ipwndfu.

For license info, check the LICENSE file.

## Compiling

`cd` into the Western source code directory, then type `chmod +x Run.sh`
or if your Compiling the C code, type `clang Western.c` or `gcc Western.c`. Either way you get something called `a.out`, that is your executable that you can run.


## Usage

Just `cd` into the Western folder with the compiled binary, then just type:  `./Western-YOUROSHERE` or for the bash script type:  `./Run.sh`, and the menu will appear. Replace the YOUROSHERE either with `Linux_x64` or `macOS_x64`.

And for the few that may have compiled the C binaries on their own, type `./a.out` or if you renamed the binary replace `a.out` with the Binary-name you renamed it to.

## Credit

* Axi0mX for ipwndfu
* planetbeing for XPwn
* Dingdongding30 on Reddit for some tips :P

## Notice

I am very much aware of C's `system();` function is easily ROPed. Also the who C executable thing is pointless, you can just run the Python file  `resources/bin/Western.py` .

