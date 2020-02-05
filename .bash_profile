export RSYNC_PROXY="172.16.2.30:8080"
export http_proxy="http://172.16.2.30:8080"
export https_proxy="http://172.16.2.30:8080"
export RSYNC_PROXY="172.16.2.30:8080"
PATH="/Library/Frameworks/Python.framework/Versions/3.7/bin:${PATH}"
export PATH

alias subl="/usr/local/bin/sublime"
# added by Miniconda3 installer
export PATH="/Users/smrititiwari/miniconda3/bin:$PATH"


#java_home setup
export JAVA_HOME=$(/usr/libexec/java_home)
export ANDROID_HOME=/home/user_directory/Android/Sdk
export PATH=${PATH}:/usr/local/mysql/bin
export PATH="/usr/local/opt/llvm/bin:$PATH"

#llvm / openMP
  export LDFLAGS="-L/usr/local/opt/llvm/lib"
  export CPPFLAGS="-I/usr/local/opt/llvm/include"
##
# Your previous /Users/smrititiwari/.bash_profile file was backed up as /Users/smrititiwari/.bash_profile.macports-saved_2019-12-05_at_20:51:38
##

# MacPorts Installer addition on 2019-12-05_at_20:51:38: adding an appropriate PATH variable for use with MacPorts.
export PATH="/opt/local/bin:/opt/local/sbin:$PATH"
# Finished adapting your PATH environment variable for use with MacPorts.


# Setting PATH for Python 3.7
export PATH="/opt/anaconda3/bin/python:$PATH"

# The original version is saved in .bash_profile.pysave


# added by Anaconda3 2019.10 installer
# >>> conda init >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$(CONDA_REPORT_ERRORS=false '/opt/anaconda3/bin/conda' shell.bash hook 2> /dev/null)"
if [ $? -eq 0 ]; then
    \eval "$__conda_setup"
else
    if [ -f "/opt/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/opt/anaconda3/etc/profile.d/conda.sh"
        CONDA_CHANGEPS1=false conda activate base
    else
        \export PATH="/opt/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda init <<<
