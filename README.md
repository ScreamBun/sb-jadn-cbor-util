# sb-jadn-cbor-util

## How to create the whl

1) From setup.py, update the version
2) Run: python setup.py bdist_wheel --universal
3) Under dist, locate: jadn_json-*-py2.py3-none-any.whl
4) Copy to the repo or project that requires this functionality
5) To add to the other project run: pip install jadn_json-*-py2.py3-none-any.whl

## Dev Setup

### Install Ruby

Refs:

- <https://stackoverflow.com/questions/37720892/you-dont-have-write-permissions-for-the-var-lib-gems-2-3-0-directory>
- <https://linuxize.com/post/how-to-install-ruby-on-ubuntu-18-04/>

1) First, update the packages index and install the packages required for the ruby-build tool to build Ruby from source

    ```cmd
    sudo apt-get remove ruby
    sudo apt update
    sudo apt install git curl libssl-dev libreadline-dev zlib1g-dev autoconf bison build-essential libyaml-dev libreadline-dev libncurses5-dev libffi-dev libgdbm-dev
    ```

2) Next, run the following curl command to install both rbenv and ruby-build

    ```cmd
    curl -sL https://github.com/rbenv/rbenv-installer/raw/main/bin/rbenv-installer | bash -
    ```

3) Add $HOME/.rbenv/bin to the system PATH.

    ```cmd
    echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(rbenv init -)"' >> ~/.bashrc
    source ~/.bashrc
    ```

    or type code ~/.bashrc to add rbenv manually

4) Install the latest stable version of Ruby and set the default version

    ```cmd
    rbenv install -l
    rbenv install 3.3.1
    rbenv global 3.3.1
    ```

5) Verify that Ruby was properly installed by printing out the version number

    ```cmd
    ruby -v
    ```

6) Install rubygems

    ```cmd
    sudo apt-get install rubygems
    ```

### Install gems

From cmdl, go to sb-jand-cbor-util, then run:

```cmd
gem install cbor-diag
```

### Conversion Commands

```cmd
json2cbor.rb -v image.json > image.cbor
cbor2json.rb -v image.cbor > image.json
cbor2diag.rb -v image.cbor > image_diag.json
cbor2pretty.rb image.cbor > image_pretty.txt
```
