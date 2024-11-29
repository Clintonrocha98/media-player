```markdown
media_player/
├── main.py                  # Ponto de entrada da aplicação
├── core/                    # Módulos centrais do sistema
│   ├── player.py            # Lógica principal do player de mídia
│   ├── playlist.py          # Gerenciamento de playlists
│   ├── metadata_extractor.py # Extração de metadados de arquivos (ex.: duração)
├── gui/                     # Interface gráfica (se houver)
│   ├── main_window.py       # Janela principal
│   ├── controls.py          # Controles do player (play, pause, stop)
│   ├── playlist_view.py     # Tela ou componente para exibir playlists
├── utils/                   # Funções auxiliares
│   ├── file_utils.py        # Manipulação de arquivos
│   ├── config.py            # Configurações globais do sistema
│   ├── logger.py            # Sistema de logs
├── tests/                   # Testes automatizados
│   ├── test_player.py       # Testes para o player
│   ├── test_playlist.py     # Testes para playlists
│   ├── test_utils.py        # Testes para funções utilitárias
├── static/                  # Recursos estáticos (ícones, imagens, etc.)
├── data/                    # Dados persistentes do sistema
│   ├── playlists/           # Arquivos de playlists salvos (ex.: JSON)
│   ├── config.json          # Configuração do sistema
├── README.md                # Documentação básica do projeto
├── requirements.txt         # Dependências do projeto (se houver)
```