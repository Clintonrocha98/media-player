
# Requisitos Funcionais

1. Leitura de Arquivos de Música:
  - O programa deve ler arquivos de música de um diretório especificado pelo
usuário.
  - Deve ser possível selecionar arquivos de música dentro do diretório.
2. Criação e Edição de Playlists:
  - As playlists devem ser armazenadas como listas encadeadas.
  - O usuário deve ser capaz de criar novas playlists editar playlists existentes.
  - Deve ser possível editar o nome das playlists.
3. Interface Gráfica:
  - O programa deve ter uma interface gráfica intuitiva e fácil de usar.
  - A interface deve permitir a exibição da lista de arquivos de música e das playlists.
  - Botões de Controle do Player:
1. Play: Inicia a reprodução da música selecionada.
2. Pause: Pausa a música em reprodução.
3. Stop: Para a música em reprodução.
4. Next: Avança para a próxima música na lista.
5. Previous: Retorna para a música anterior na lista.
6. Randômico: Randomiza a lista de músicas.
  - A interface deve incluir opções para criar e editar playlists.
4. Execução de Músicas:
  - O programa deve ser capaz de executar as músicas em ordem sequencial.
  - Deve haver uma opção para executar as músicas em ordem aleatória (randômica).
  - O usuário deve poder randomizar a ordem das músicas em uma playlist escolhida.
  - As estruturas das playlists devem ser armazenadas em arquivos para manter as playlists criadas

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

