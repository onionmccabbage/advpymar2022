# we can run pyttest to test this module
# may need to pip install pytest

from collections import namedtuple

# our 'task' tuple will contain a summary, an owner, a 'done' and an id field
# a named tuple lets us ensure these members exist
task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
# we can set sensible default values for the members
task.__new__.__defaults__ = (None, None, False, None)

def test_defaults():
    t = task() # this will use the defaults
    s = task(None, None, False, None)
    # print(t==s)
    # we can use pytest to assert outcomes
    assert t==s

# pytests will look for any function beginning with 'test'
def test_member_access():
    t = task('Coffee break', 'Grace')
    # print(t.summary, t.owner)
    assert t.summary == 'Coffee break'
    assert t.owner == 'Grace'
    assert (t.done, t.id) == (False, None)

if __name__ == '__main__':
    test_defaults()
    test_member_access()