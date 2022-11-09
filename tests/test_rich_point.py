from unittest import TestCase, main

from logger_utility import RichPoint


class TestRichPoint(TestCase):
    def test_copy(self) -> None:
        r = RichPoint("test").tag("foo", 1).field("bar", 2)
        c = r.copy().tag("foobar", 3).field("barfoo", 4)

        assert r._name == c._name
        assert r._tags != c._tags
        assert r._fields != c._fields

        assert "foo" in r._tags
        assert "foo" in c._tags
        assert "foobar" not in r._tags
        assert "foobar" in c._tags


if __name__ == "__main__":
    main()
