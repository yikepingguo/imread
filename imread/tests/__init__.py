def run(verbose=False):
    import nose
    from os import path
    currentdir = path.dirname(__file__)
    updir = path.join(currentdir, '..')
    argv = ['', '--exe', '-w', updir]
    if verbose:
        argv.append('--verbose')
    nose.run('imread', argv=argv)

def file_path(fname):
    return 'imread/tests/data/'+fname
