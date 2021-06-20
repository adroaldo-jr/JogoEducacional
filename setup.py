import cx_Freeze

executables = [cx_Freeze.Executable(script="jogoEducacional.py", icon="assets/lionIcon.png")]

cx_Freeze.setup (
    name = "Jogo Educacional - Coma as vogais",
    options = {"build_exe": {"packages": ["pygame"],
    "include_files":["assets"]}},
    executables = executables
)