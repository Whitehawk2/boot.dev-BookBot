{ pkgs, ... }:

{
  # https://devenv.sh/basics/
  env.GREET = "devenv";

  # https://devenv.sh/packages/
  packages = [ pkgs.gh ];

  # https://devenv.sh/scripts/
  #scripts.hello.exec = "echo hello from $GREET";

  enterShell = ''
  [[ -d ../BookBotvenv ]] || python3 -m venv ../BookBotvenv
  source ../BookBotvenv/bin/activate
  '';

  # https://devenv.sh/tests/
  #enterTest = ''
  #  echo "Running tests"
  #  git --version | grep "2.42.0"
  #'';

  # https://devenv.sh/services/
  # services.postgres.enable = true;

  # https://devenv.sh/languages/
  # languages.nix.enable = true;
  #languages.python.enable = true;
  #languages.python.venv.enable = true;
  #languages.python.venv.quiet.enable = true;

  # https://devenv.sh/pre-commit-hooks/
  # pre-commit.hooks.shellcheck.enable = true;

  # https://devenv.sh/processes/
  # processes.ping.exec = "ping example.com";

  # See full reference at https://devenv.sh/reference/options/
}
