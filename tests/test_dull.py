from dull import profile


def test_profile_to_console(capsys):
    @profile()
    def foo():
        return

    foo()
    out = capsys.readouterr()

    assert "profile" in out.err


def test_profile_to_file(tmpdir, capsys):
    @profile(to_file=True, name="test", folder=tmpdir)
    def foo():
        return

    foo()

    out = capsys.readouterr()
    assert "profile saved to" in out.err

    assert tmpdir.join("test.dat").exists()
