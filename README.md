# apple_ssv
Adventures in Apple Signed System Volumes (SSV)


## Format

### mtree.i.txt

* Lines begining with `#` are comments and not processed
* Lines which are entirely whitespace are ignored
* Lines ending with `\` are continued with the following line (ignore the linefeed)
* Lines starting with `/` are directives and processed
    * The directive `/set` set's the defaults for each node
* Lines starting with non-whitespace navigate to a directory
* Lines starting with whitespace create child nodes
* Lines can contain either a name followed by key/value pairs or whitespace and then key/value pairs
* Lines can naviage to `.` or `..` which set properties on the current object and stay or set values on the parent and 
  navigate up the tree
* `xattrdigest` is a SHA256 hash, a period and the hash salt (64-bit?)
* All `siblingid`s seem to be zero
* The `type` attribute can be `link`, `file` or `dir`
* Link nodes are linked by inode