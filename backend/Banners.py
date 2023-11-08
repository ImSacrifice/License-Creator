import shutil

center = shutil.get_terminal_size().columns

_banner = """
╦  ┬┌─┐┌─┐┌┐┌┌─┐┌─┐
║  ││  ├┤ │││└─┐├┤ 
╩═╝┴└─┘└─┘┘└┘└─┘└─┘
╔═╗┬─┐┌─┐┌─┐┌┬┐┌─┐┬─┐
║  ├┬┘├┤ ├─┤ │ │ │├┬┘
╚═╝┴└─└─┘┴ ┴ ┴ └─┘┴└─

Made by Sacrifice.zip

"""

banner = "\n".join(line.center(center) for line in _banner.splitlines())
