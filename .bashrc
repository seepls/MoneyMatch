export RSYNC_PROXY="172.16.2.30:8080"

export http_proxy="http://172.16.2.30:8080"
export https_proxy="http://172.16.2.30:8080"
export RSYNC_PROXY="172.16.2.30:8080"
export PATH=~/anaconda3/bin:$PATH

alias subl="/usr/local/bin/sublime"
JAVA_HOME=/Library/Java/Home
export JAVA_HOME;
export ANDROID_HOME=/home/user_directory/Android/Sdk
export PATH=${PATH}:/usr/local/mysql/bin


#llvm/ openmp
  export LDFLAGS="-L/usr/local/opt/llvm/lib"
  export CPPFLAGS="-I/usr/local/opt/llvm/include" 




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

# python 3.7
 export PATH="/opt/anaconda3/bin/python:$PATH"
# export PATH
