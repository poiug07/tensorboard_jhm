import argparse
import uuid

from IPython.display import HTML, display
import jupyter_tensorboard


def _tensorboard_magic(line):
    """Line magic function.
    Makes an AJAX call to the Jupyter TensorBoard server extension and outputs
    an IFrame displaying the TensorBoard instance.
    """
#     print(dir(jupyter_tensorboard.handlers))

    parser = argparse.ArgumentParser()
    parser.add_argument("--logdir", default="/workspace/")
    parser.add_argument("--h", default=620)
    args = parser.parse_args(line.split())

    iframe_id = "tensorboard-" + str(uuid.uuid4())
    
    html = """
<!-- JUPYTER_TENSORBOARD_TEST_MARKER -->
<script>
    // Token is required to spawn new instance if not present
    // New tensorboard instance is not spawned if it exists in given dir
    var xsrfToken = document.cookie.match(new RegExp('(^| )_xsrf=([^;]+)'));
    xsrfToken = xsrfToken ? xsrfToken[2] : undefined;
    var logdir = '%s';
    if (logdir=='.'){
        logdir = Jupyter.notebook.base_url;
        logdir = logdir.replace("user", "home")
    } else {
        logdir = Jupyter.notebook.base_url + logdir;
    }
    fetch(Jupyter.notebook.base_url + 'api/tensorboard', {
        method: 'POST',
        credentials: 'include',
        headers: {
            "Content-Type": "application/json",
            "X-Requested-With": "XMLHttpRequest",
            "X-XSRFToken": xsrfToken,
        },
        body: JSON.stringify({'logdir': logdir}),
    })
        .then(res => res.json())
        .then(res => {
            const iframe = document.getElementById('%s');
            iframe.style.height = '%spx';
            iframe.src = Jupyter.notebook.base_url + 'tensorboard/' + res.name;
            iframe.style.display = 'block';
            /*
            for(let i=0; i<res.length; i++) {
                if (res[i].logdir==logdir){
                    var obj = res[i];
                    iframe.src = Jupyter.notebook.base_url + 'tensorboard/' + obj.name;
                    iframe.style.display = 'block';
                    return;
                }
            }
            console.log("Tensoboard instance with given directory not found.");
            iframe.contentWindow.document.open('text/htmlreplace');
            iframe.contentWindow.document.write("Error: Tensorboard instance with given directory not found.");
            iframe.contentWindow.document.close();
            iframe.style.height = '50px';
            iframe.style.display = 'block';
            */
        });
</script>
<iframe
    id="%s"
    style="width: 100%%; height: 620px; display: none;"
    frameBorder="0">
</iframe>
""" % (
        args.logdir,
        iframe_id,
        args.h,
        iframe_id,
    )

    display(HTML(html))


def load_ipython_extension(ipython):
    """Deprecated: use `%load_ext tensorboard` instead.
    Raises:
      RuntimeError: Always.
    """
    raise RuntimeError(
        "Use '%load_ext tensorboard' instead of '%load_ext tensorboard.notebook'."
    )


def _load_ipython_extension(ipython):
    """Load the TensorBoard notebook extension.
    Intended to be called from `%load_ext tensorboard`. Do not invoke this
    directly.
    Args:
      ipython: An `IPython.InteractiveShell` instance.
    """
    ipython.register_magic_function(
        _tensorboard_magic,
        magic_kind="line",
        magic_name="tensorboard",
    )