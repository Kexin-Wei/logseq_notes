- Package manager
	- Lazy.nvim
		- [Zero to IDE with LazyVim](https://www.youtube.com/watch?v=N93cTbtLCIM)
	- [Migrate from packer](https://github.com/folke/lazy.nvim#-migration-guide)
		- `setup` ➡️ `init`
		- `requires` ➡️ `dependencies`
		- `as` ➡️ `name`
		- `opt` ➡️ `lazy`
		- `run` ➡️ `build`
		- `lock` ➡️ `pin`
		- `disable=true` ➡️ `enabled = false`
		- `tag='*'` ➡️ `version="*"`
		- `after` ℹ️ ***not needed*** for most use-cases. Use `dependencies` otherwise.
		- `wants` ℹ️ ***not needed*** for most use-cases. Use `dependencies` otherwise.
		- `config` don't support string type, use `fun(LazyPlugin)` instead.
		- `module` is auto-loaded. No need to specify
		- `keys` spec is [different](https://github.com/folke/lazy.nvim#%EF%B8%8F-lazy-key-mappings)
		- `rtp` can be accomplished with:
		- ```
		  config = function(plugin)
		    vim.opt.rtp:append(plugin.dir .. "/custom-rtp")
		  end
		  ```
		- With packer `wants`, `requires` and `after` can be used to manage dependencies. With lazy, this isn't needed for most of the Lua dependencies. They can be installed just like normal plugins (even with `lazy=true`) and will be loaded when other plugins need them. The `dependencies` key can be used to group those required plugins with the one that requires them. The plugins which are added as `dependencies` will always be lazy-loaded and loaded when the plugin is loaded.
- LSP: build your IDE
	- [A great concept explaining blog](https://roobert.github.io/2022/12/03/Extending-Neovim/)
	- Mason
	- null-ls
		- https://smarttech101.com/nvim-lsp-set-up-null-ls-for-beginners/
- Python
	- [Python and pyenv - Schlink's Docs (sts10.github.io)](https://sts10.github.io/docs/initial-setup/dev-env/python-pyenv.html)
	- [How to set python interpreter in neovim for python language server depending on pyenv / virtualenv - Stack Overflow](https://stackoverflow.com/questions/65847159/how-to-set-python-interpreter-in-neovim-for-python-language-server-depending-on)
	- [Setting up Python for Neovim · deoplete-plugins/deoplete-jedi Wiki (github.com)](https://github.com/deoplete-plugins/deoplete-jedi/wiki/Setting-up-Python-for-Neovim)
	
