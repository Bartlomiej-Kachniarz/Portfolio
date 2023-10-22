from airflow.decorators import task


@task.virtualenv(
    task_id="virtualenv_python",
    requirements=["colorama==0.4.0"],
    system_site_packages=False,
)
def callable_virtualenv():
    """
    Example function that will be performed in a virtual environment.

    Importing at the module level ensures that it will not attempt to import the
    library before it is installed.
    """

    from time import sleep

    from colorama import Back, Fore, Style

    print(Fore.RED + "this is a text in red")
    print(Back.GREEN + "on a green background")
    print(Style.DIM + "in dim text")
    print(Style.RESET_ALL)

    for _ in range(4):
        print(Style.DIM + "Please wait a second...", flush=True)
        sleep(1)
    print("Finished")


virtual_env_task = callable_virtualenv()
