cat <<EOF > $HOME/.pypirc
[distutils]
index-servers = 
    pypi

[pypi]
username:$PYPI_USER
password:$PYPI_PASS
EOF
