# Libraries

| Name                     | Description |
|--------------------------|-------------|
| *libmoneyrocket_cli*         | RPC client functionality used by *moneyrocket-cli* executable |
| *libmoneyrocket_common*      | Home for common functionality shared by different executables and libraries. Similar to *libmoneyrocket_util*, but higher-level (see [Dependencies](#dependencies)). |
| *libmoneyrocket_consensus*   | Stable, backwards-compatible consensus functionality used by *libmoneyrocket_node* and *libmoneyrocket_wallet* and also exposed as a [shared library](../shared-libraries.md). |
| *libmoneyrocketconsensus*    | Shared library build of static *libmoneyrocket_consensus* library |
| *libmoneyrocket_kernel*      | Consensus engine and support library used for validation by *libmoneyrocket_node* and also exposed as a [shared library](../shared-libraries.md). |
| *libmoneyrocketqt*           | GUI functionality used by *moneyrocket-qt* and *moneyrocket-gui* executables |
| *libmoneyrocket_ipc*         | IPC functionality used by *moneyrocket-node*, *moneyrocket-wallet*, *moneyrocket-gui* executables to communicate when [`--enable-multiprocess`](multiprocess.md) is used. |
| *libmoneyrocket_node*        | P2P and RPC server functionality used by *moneyrocketd* and *moneyrocket-qt* executables. |
| *libmoneyrocket_util*        | Home for common functionality shared by different executables and libraries. Similar to *libmoneyrocket_common*, but lower-level (see [Dependencies](#dependencies)). |
| *libmoneyrocket_wallet*      | Wallet functionality used by *moneyrocketd* and *moneyrocket-wallet* executables. |
| *libmoneyrocket_wallet_tool* | Lower-level wallet functionality used by *moneyrocket-wallet* executable. |
| *libmoneyrocket_zmq*         | [ZeroMQ](../zmq.md) functionality used by *moneyrocketd* and *moneyrocket-qt* executables. |

## Conventions

- Most libraries are internal libraries and have APIs which are completely unstable! There are few or no restrictions on backwards compatibility or rules about external dependencies. Exceptions are *libmoneyrocket_consensus* and *libmoneyrocket_kernel* which have external interfaces documented at [../shared-libraries.md](../shared-libraries.md).

- Generally each library should have a corresponding source directory and namespace. Source code organization is a work in progress, so it is true that some namespaces are applied inconsistently, and if you look at [`libmoneyrocket_*_SOURCES`](../../src/Makefile.am) lists you can see that many libraries pull in files from outside their source directory. But when working with libraries, it is good to follow a consistent pattern like:

  - *libmoneyrocket_node* code lives in `src/node/` in the `node::` namespace
  - *libmoneyrocket_wallet* code lives in `src/wallet/` in the `wallet::` namespace
  - *libmoneyrocket_ipc* code lives in `src/ipc/` in the `ipc::` namespace
  - *libmoneyrocket_util* code lives in `src/util/` in the `util::` namespace
  - *libmoneyrocket_consensus* code lives in `src/consensus/` in the `Consensus::` namespace

## Dependencies

- Libraries should minimize what other libraries they depend on, and only reference symbols following the arrows shown in the dependency graph below:

<table><tr><td>

```mermaid

%%{ init : { "flowchart" : { "curve" : "basis" }}}%%

graph TD;

moneyrocket-cli[moneyrocket-cli]-->libmoneyrocket_cli;

moneyrocketd[moneyrocketd]-->libmoneyrocket_node;
moneyrocketd[moneyrocketd]-->libmoneyrocket_wallet;

moneyrocket-qt[moneyrocket-qt]-->libmoneyrocket_node;
moneyrocket-qt[moneyrocket-qt]-->libmoneyrocketqt;
moneyrocket-qt[moneyrocket-qt]-->libmoneyrocket_wallet;

moneyrocket-wallet[moneyrocket-wallet]-->libmoneyrocket_wallet;
moneyrocket-wallet[moneyrocket-wallet]-->libmoneyrocket_wallet_tool;

libmoneyrocket_cli-->libmoneyrocket_util;
libmoneyrocket_cli-->libmoneyrocket_common;

libmoneyrocket_common-->libmoneyrocket_consensus;
libmoneyrocket_common-->libmoneyrocket_util;

libmoneyrocket_kernel-->libmoneyrocket_consensus;
libmoneyrocket_kernel-->libmoneyrocket_util;

libmoneyrocket_node-->libmoneyrocket_consensus;
libmoneyrocket_node-->libmoneyrocket_kernel;
libmoneyrocket_node-->libmoneyrocket_common;
libmoneyrocket_node-->libmoneyrocket_util;

libmoneyrocketqt-->libmoneyrocket_common;
libmoneyrocketqt-->libmoneyrocket_util;

libmoneyrocket_wallet-->libmoneyrocket_common;
libmoneyrocket_wallet-->libmoneyrocket_util;

libmoneyrocket_wallet_tool-->libmoneyrocket_wallet;
libmoneyrocket_wallet_tool-->libmoneyrocket_util;

classDef bold stroke-width:2px, font-weight:bold, font-size: smaller;
class moneyrocket-qt,moneyrocketd,moneyrocket-cli,moneyrocket-wallet bold
```
</td></tr><tr><td>

**Dependency graph**. Arrows show linker symbol dependencies. *Consensus* lib depends on nothing. *Util* lib is depended on by everything. *Kernel* lib depends only on consensus and util.

</td></tr></table>

- The graph shows what _linker symbols_ (functions and variables) from each library other libraries can call and reference directly, but it is not a call graph. For example, there is no arrow connecting *libmoneyrocket_wallet* and *libmoneyrocket_node* libraries, because these libraries are intended to be modular and not depend on each other's internal implementation details. But wallet code is still able to call node code indirectly through the `interfaces::Chain` abstract class in [`interfaces/chain.h`](../../src/interfaces/chain.h) and node code calls wallet code through the `interfaces::ChainClient` and `interfaces::Chain::Notifications` abstract classes in the same file. In general, defining abstract classes in [`src/interfaces/`](../../src/interfaces/) can be a convenient way of avoiding unwanted direct dependencies or circular dependencies between libraries.

- *libmoneyrocket_consensus* should be a standalone dependency that any library can depend on, and it should not depend on any other libraries itself.

- *libmoneyrocket_util* should also be a standalone dependency that any library can depend on, and it should not depend on other internal libraries.

- *libmoneyrocket_common* should serve a similar function as *libmoneyrocket_util* and be a place for miscellaneous code used by various daemon, GUI, and CLI applications and libraries to live. It should not depend on anything other than *libmoneyrocket_util* and *libmoneyrocket_consensus*. The boundary between _util_ and _common_ is a little fuzzy but historically _util_ has been used for more generic, lower-level things like parsing hex, and _common_ has been used for moneyrocket-specific, higher-level things like parsing base58. The difference between util and common is mostly important because *libmoneyrocket_kernel* is not supposed to depend on *libmoneyrocket_common*, only *libmoneyrocket_util*. In general, if it is ever unclear whether it is better to add code to *util* or *common*, it is probably better to add it to *common* unless it is very generically useful or useful particularly to include in the kernel.


- *libmoneyrocket_kernel* should only depend on *libmoneyrocket_util* and *libmoneyrocket_consensus*.

- The only thing that should depend on *libmoneyrocket_kernel* internally should be *libmoneyrocket_node*. GUI and wallet libraries *libmoneyrocketqt* and *libmoneyrocket_wallet* in particular should not depend on *libmoneyrocket_kernel* and the unneeded functionality it would pull in, like block validation. To the extent that GUI and wallet code need scripting and signing functionality, they should be get able it from *libmoneyrocket_consensus*, *libmoneyrocket_common*, and *libmoneyrocket_util*, instead of *libmoneyrocket_kernel*.

- GUI, node, and wallet code internal implementations should all be independent of each other, and the *libmoneyrocketqt*, *libmoneyrocket_node*, *libmoneyrocket_wallet* libraries should never reference each other's symbols. They should only call each other through [`src/interfaces/`](`../../src/interfaces/`) abstract interfaces.

## Work in progress

- Validation code is moving from *libmoneyrocket_node* to *libmoneyrocket_kernel* as part of [The libmoneyrocketkernel Project #24303](https://github.com/moneyrocket/moneyrocket/issues/24303)
- Source code organization is discussed in general in [Library source code organization #15732](https://github.com/moneyrocket/moneyrocket/issues/15732)
