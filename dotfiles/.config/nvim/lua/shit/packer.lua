vim.cmd [[packadd packer.nvim]]

return require('packer').startup(function(use)
    -- Packer can manage itself
    use 'wbthomason/packer.nvim'

    use {
        'nvim-telescope/telescope.nvim', tag = '0.1.8',
        -- or                            , branch = '0.1.x',
        requires = { { 'nvim-lua/plenary.nvim' } }
    }

    use({
        "olimorris/onedarkpro.nvim",
        as = "onedark",
        config = function()
            vim.cmd("colorscheme onedark")
        end
    })
    use('nvim-treesitter/nvim-treesitter', { run = ':TSUpdate' })
    use('nvim-treesitter/playground')
    use('ThePrimeagen/harpoon')
    use('mbbill/undotree')
    use {
        'VonHeikemen/lsp-zero.nvim', -- lsp-zero framework
        branch = 'v2.x',
        requires = {
            -- Required LSP plugins
            { 'neovim/nvim-lspconfig' },  -- Core LSP configuration
            { 'williamboman/mason.nvim' }, -- LSP server manager
            { 'williamboman/mason-lspconfig.nvim' }, -- Bridges Mason and lspconfig
            { 'hrsh7th/nvim-cmp' },       -- Autocompletion
            { 'hrsh7th/cmp-nvim-lsp' },   -- LSP completions
        }
    }
    use({
        "nvim-neo-tree/neo-tree.nvim",
        branch = "v3.x",
        requires = {
            "nvim-lua/plenary.nvim",
            "nvim-tree/nvim-web-devicons", -- not strictly required, but recommended
            "MunifTanjim/nui.nvim",
            -- "3rd/image.nvim", -- Optional image support in preview window: See `# Preview Mode` for more information
        }
    })
end)
