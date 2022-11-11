# Instalacion en Linux

## Instalar virtualenv

~~~bash
sudo apt-get install python3-pip
sudo pip3 install virtualenv
~~~

## Instalar sqlite

~~~bash
sudo apt-get install sqlite3
~~~

## Clonar repo

~~~bash
# Mediante protocolo https
git clone https://github.com/fabriciojallaza/zb_backend.git

# Mediante protocolo ssh
git clone git@github.com:fabriciojallaza/zb_backend.git
~~~

## Creamos en entorno virtual

~~~bash
python3 -m virtualenv venv
~~~

## Instalación de dependencias

### Activamos el virtualenv:

~~~bash
source venv/local/bin/activate
~~~

### Instalamos los requerimientos

~~~bash
pip install -r requirements.txt
~~~

### Corremos el Proyecto:

~~~bash
python manage.py runserver
~~~

## Working tree

~~~bash
.
├── catalog_system
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── settings.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── wsgi.cpython-310.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_user_email.py
│   │   ├── 0003_alter_user_email.py
│   │   ├── 0004_user_is_staff.py
│   │   ├── 0005_auto_20221110_0933.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-310.pyc
│   │       ├── 0002_alter_user_email.cpython-310.pyc
│   │       ├── 0003_alter_user_email.cpython-310.pyc
│   │       ├── 0004_user_is_staff.cpython-310.pyc
│   │       ├── 0005_auto_20221110_0933.cpython-310.pyc
│   │       └── __init__.cpython-310.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-310.pyc
│   │   ├── apps.cpython-310.pyc
│   │   ├── __init__.cpython-310.pyc
│   │   ├── models.cpython-310.pyc
│   │   └── tests.cpython-310.pyc
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── products
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-310.pyc
│   │       └── __init__.cpython-310.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-310.pyc
│   │   ├── apps.cpython-310.pyc
│   │   ├── __init__.cpython-310.pyc
│   │   ├── models.cpython-310.pyc
│   │   ├── serializers.cpython-310.pyc
│   │   ├── tests.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── views.cpython-310.pyc
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── __pycache__
│   └── manage.cpython-310.pyc
├── README.md
├── requirements.txt
├── user
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-310.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-310.pyc
│   │   ├── apps.cpython-310.pyc
│   │   ├── __init__.cpython-310.pyc
│   │   ├── models.cpython-310.pyc
│   │   ├── serializers.cpython-310.pyc
│   │   ├── tests.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── views.cpython-310.pyc
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── utils
│   ├── email_handler.py
│   └── __pycache__
│       └── email_handler.cpython-310.pyc
└── venv
    ├── lib
    │   └── python3.10
    ├── local
    │   ├── bin
    │   │   ├── activate
    │   │   ├── activate.csh
    │   │   ├── activate.fish
    │   │   ├── activate.ps1
    │   │   ├── activate_this.py
    │   │   ├── activate.xsh
    │   │   ├── easy_install
    │   │   ├── easy_install3
    │   │   ├── easy_install-3.10
    │   │   ├── pip
    │   │   ├── pip3
    │   │   ├── pip-3.10
    │   │   ├── pip3.10
    │   │   ├── python -> /usr/bin/python3.10
    │   │   ├── python3 -> python
    │   │   ├── python3.10 -> python
    │   │   ├── wheel
    │   │   ├── wheel3
    │   │   └── wheel-3.10
    │   └── lib
    │       └── python3.10
    │           └── dist-packages
    │               ├── easy_install.py
    │               ├── pip
    │               │   ├── __init__.py
    │               │   ├── _internal
    │               │   │   ├── build_env.py
    │               │   │   ├── cache.py
    │               │   │   ├── cli
    │               │   │   │   ├── autocompletion.py
    │               │   │   │   ├── base_command.py
    │               │   │   │   ├── cmdoptions.py
    │               │   │   │   ├── command_context.py
    │               │   │   │   ├── __init__.py
    │               │   │   │   ├── main_parser.py
    │               │   │   │   ├── main.py
    │               │   │   │   ├── parser.py
    │               │   │   │   ├── req_command.py
    │               │   │   │   └── status_codes.py
    │               │   │   ├── commands
    │               │   │   │   ├── check.py
    │               │   │   │   ├── completion.py
    │               │   │   │   ├── configuration.py
    │               │   │   │   ├── debug.py
    │               │   │   │   ├── download.py
    │               │   │   │   ├── freeze.py
    │               │   │   │   ├── hash.py
    │               │   │   │   ├── help.py
    │               │   │   │   ├── __init__.py
    │               │   │   │   ├── install.py
    │               │   │   │   ├── list.py
    │               │   │   │   ├── search.py
    │               │   │   │   ├── show.py
    │               │   │   │   ├── uninstall.py
    │               │   │   │   └── wheel.py
    │               │   │   ├── configuration.py
    │               │   │   ├── distributions
    │               │   │   │   ├── base.py
    │               │   │   │   ├── __init__.py
    │               │   │   │   ├── installed.py
    │               │   │   │   ├── sdist.py
    │               │   │   │   └── wheel.py
    │               │   │   ├── exceptions.py
    │               │   │   ├── index
    │               │   │   │   ├── collector.py
    │               │   │   │   ├── __init__.py
    │               │   │   │   └── package_finder.py
    │               │   │   ├── __init__.py
    │               │   │   ├── legacy_resolve.py
    │               │   │   ├── locations.py
    │               │   │   ├── main.py
    │               │   │   ├── models
    │               │   │   │   ├── candidate.py
    │               │   │   │   ├── format_control.py
    │               │   │   │   ├── index.py
    │               │   │   │   ├── __init__.py
    │               │   │   │   ├── link.py
    │               │   │   │   ├── scheme.py
    │               │   │   │   ├── search_scope.py
    │               │   │   │   ├── selection_prefs.py
    │               │   │   │   ├── target_python.py
    │               │   │   │   └── wheel.py
    │               │   │   ├── network
    │               │   │   │   ├── auth.py
    │               │   │   │   ├── cache.py
    │               │   │   │   ├── download.py
    │               │   │   │   ├── __init__.py
    │               │   │   │   ├── session.py
    │               │   │   │   ├── utils.py
    │               │   │   │   └── xmlrpc.py
    │               │   │   ├── operations
    │               │   │   │   ├── build
    │               │   │   │   │   ├── __init__.py
    │               │   │   │   │   ├── metadata_legacy.py
    │               │   │   │   │   ├── metadata.py
    │               │   │   │   │   ├── wheel_legacy.py
    │               │   │   │   │   └── wheel.py
    │               │   │   │   ├── check.py
    │               │   │   │   ├── freeze.py
    │               │   │   │   ├── __init__.py
    │               │   │   │   ├── install
    │               │   │   │   │   ├── editable_legacy.py
    │               │   │   │   │   ├── __init__.py
    │               │   │   │   │   ├── legacy.py
    │               │   │   │   │   └── wheel.py
    │               │   │   │   └── prepare.py
    │               │   │   ├── pep425tags.py
    │               │   │   ├── pyproject.py
    │               │   │   ├── req
    │               │   │   │   ├── constructors.py
    │               │   │   │   ├── __init__.py
    │               │   │   │   ├── req_file.py
    │               │   │   │   ├── req_install.py
    │               │   │   │   ├── req_set.py
    │               │   │   │   ├── req_tracker.py
    │               │   │   │   └── req_uninstall.py
    │               │   │   ├── self_outdated_check.py
    │               │   │   ├── utils
    │               │   │   │   ├── appdirs.py
    │               │   │   │   ├── compat.py
    │               │   │   │   ├── deprecation.py
    │               │   │   │   ├── distutils_args.py
    │               │   │   │   ├── encoding.py
    │               │   │   │   ├── entrypoints.py
    │               │   │   │   ├── filesystem.py
    │               │   │   │   ├── filetypes.py
    │               │   │   │   ├── glibc.py
    │               │   │   │   ├── hashes.py
    │               │   │   │   ├── __init__.py
    │               │   │   │   ├── inject_securetransport.py
    │               │   │   │   ├── logging.py
    │               │   │   │   ├── marker_files.py
    │               │   │   │   ├── misc.py
    │               │   │   │   ├── models.py
    │               │   │   │   ├── packaging.py
    │               │   │   │   ├── pkg_resources.py
    │               │   │   │   ├── setuptools_build.py
    │               │   │   │   ├── subprocess.py
    │               │   │   │   ├── temp_dir.py
    │               │   │   │   ├── typing.py
    │               │   │   │   ├── ui.py
    │               │   │   │   ├── unpacking.py
    │               │   │   │   ├── urls.py
    │               │   │   │   ├── virtualenv.py
    │               │   │   │   └── wheel.py
    │               │   │   ├── vcs
    │               │   │   │   ├── bazaar.py
    │               │   │   │   ├── git.py
    │               │   │   │   ├── __init__.py
    │               │   │   │   ├── mercurial.py
    │               │   │   │   ├── subversion.py
    │               │   │   │   └── versioncontrol.py
    │               │   │   └── wheel_builder.py
    │               │   ├── __main__.py
    │               │   └── _vendor
    │               │       └── __init__.py
    │               ├── pip-20.0.2.dist-info
    │               │   ├── entry_points.txt
    │               │   ├── INSTALLER
    │               │   ├── LICENSE.txt
    │               │   ├── METADATA
    │               │   ├── RECORD
    │               │   ├── top_level.txt
    │               │   └── WHEEL
    │               ├── pip-20.0.2.virtualenv
    │               ├── pkg_resources
    │               │   ├── extern
    │               │   │   └── __init__.py
    │               │   ├── __init__.py
    │               │   ├── py31compat.py
    │               │   └── _vendor
    │               │       ├── appdirs.py
    │               │       ├── __init__.py
    │               │       ├── packaging
    │               │       │   ├── __about__.py
    │               │       │   ├── _compat.py
    │               │       │   ├── __init__.py
    │               │       │   ├── markers.py
    │               │       │   ├── requirements.py
    │               │       │   ├── specifiers.py
    │               │       │   ├── _structures.py
    │               │       │   ├── utils.py
    │               │       │   └── version.py
    │               │       ├── pyparsing.py
    │               │       └── six.py
    │               ├── pkg_resources-0.0.0.dist-info
    │               │   ├── AUTHORS.txt
    │               │   ├── INSTALLER
    │               │   ├── LICENSE.txt
    │               │   ├── METADATA
    │               │   ├── RECORD
    │               │   └── WHEEL
    │               ├── pkg_resources-0.0.0.virtualenv
    │               ├── setuptools
    │               │   ├── archive_util.py
    │               │   ├── build_meta.py
    │               │   ├── cli-32.exe
    │               │   ├── cli-64.exe
    │               │   ├── cli.exe
    │               │   ├── command
    │               │   │   ├── alias.py
    │               │   │   ├── bdist_egg.py
    │               │   │   ├── bdist_rpm.py
    │               │   │   ├── bdist_wininst.py
    │               │   │   ├── build_clib.py
    │               │   │   ├── build_ext.py
    │               │   │   ├── build_py.py
    │               │   │   ├── develop.py
    │               │   │   ├── dist_info.py
    │               │   │   ├── easy_install.py
    │               │   │   ├── egg_info.py
    │               │   │   ├── __init__.py
    │               │   │   ├── install_egg_info.py
    │               │   │   ├── install_lib.py
    │               │   │   ├── install.py
    │               │   │   ├── install_scripts.py
    │               │   │   ├── launcher manifest.xml
    │               │   │   ├── py36compat.py
    │               │   │   ├── register.py
    │               │   │   ├── rotate.py
    │               │   │   ├── saveopts.py
    │               │   │   ├── sdist.py
    │               │   │   ├── setopt.py
    │               │   │   ├── test.py
    │               │   │   ├── upload_docs.py
    │               │   │   └── upload.py
    │               │   ├── config.py
    │               │   ├── depends.py
    │               │   ├── _deprecation_warning.py
    │               │   ├── dep_util.py
    │               │   ├── dist.py
    │               │   ├── errors.py
    │               │   ├── extension.py
    │               │   ├── extern
    │               │   │   └── __init__.py
    │               │   ├── glob.py
    │               │   ├── gui-32.exe
    │               │   ├── gui-64.exe
    │               │   ├── gui.exe
    │               │   ├── _imp.py
    │               │   ├── __init__.py
    │               │   ├── installer.py
    │               │   ├── launch.py
    │               │   ├── lib2to3_ex.py
    │               │   ├── monkey.py
    │               │   ├── msvc.py
    │               │   ├── namespaces.py
    │               │   ├── package_index.py
    │               │   ├── py27compat.py
    │               │   ├── py31compat.py
    │               │   ├── py33compat.py
    │               │   ├── py34compat.py
    │               │   ├── sandbox.py
    │               │   ├── script (dev).tmpl
    │               │   ├── script.tmpl
    │               │   ├── site-patch.py
    │               │   ├── ssl_support.py
    │               │   ├── unicode_utils.py
    │               │   ├── _vendor
    │               │   │   ├── __init__.py
    │               │   │   ├── ordered_set.py
    │               │   │   ├── packaging
    │               │   │   │   ├── __about__.py
    │               │   │   │   ├── _compat.py
    │               │   │   │   ├── __init__.py
    │               │   │   │   ├── markers.py
    │               │   │   │   ├── requirements.py
    │               │   │   │   ├── specifiers.py
    │               │   │   │   ├── _structures.py
    │               │   │   │   ├── tags.py
    │               │   │   │   ├── utils.py
    │               │   │   │   └── version.py
    │               │   │   ├── pyparsing.py
    │               │   │   └── six.py
    │               │   ├── version.py
    │               │   ├── wheel.py
    │               │   └── windows_support.py
    │               ├── setuptools-44.0.0.dist-info
    │               │   ├── AUTHORS.txt
    │               │   ├── dependency_links.txt
    │               │   ├── entry_points.txt
    │               │   ├── INSTALLER
    │               │   ├── LICENSE.txt
    │               │   ├── METADATA
    │               │   ├── RECORD
    │               │   ├── top_level.txt
    │               │   ├── WHEEL
    │               │   └── zip-safe
    │               ├── setuptools-44.0.0.virtualenv
    │               ├── _virtualenv.pth
    │               ├── _virtualenv.py
    │               ├── wheel
    │               │   ├── bdist_wheel.py
    │               │   ├── cli
    │               │   │   ├── convert.py
    │               │   │   ├── __init__.py
    │               │   │   ├── pack.py
    │               │   │   └── unpack.py
    │               │   ├── __init__.py
    │               │   ├── macosx_libfile.py
    │               │   ├── __main__.py
    │               │   ├── metadata.py
    │               │   ├── pep425tags.py
    │               │   ├── pkginfo.py
    │               │   ├── util.py
    │               │   ├── _version.py
    │               │   └── wheelfile.py
    │               ├── wheel-0.34.2.dist-info
    │               │   ├── AUTHORS.txt
    │               │   ├── entry_points.txt
    │               │   ├── INSTALLER
    │               │   ├── LICENSE.txt
    │               │   ├── METADATA
    │               │   ├── RECORD
    │               │   ├── top_level.txt
    │               │   └── WHEEL
    │               └── wheel-0.34.2.virtualenv
    └── pyvenv.cfg

55 directories, 362 files
