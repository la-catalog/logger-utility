from unittest import TestCase, main

from logger_utility import RichPoint


class TestRichPoint(TestCase):
    def test_copy(self) -> None:
        r = RichPoint("test").tag("foo", 1).field("bar", 2)
        c = r.copy().tag("foobar", 3).field("barfoo", 4)

        print(r.to_line_protocol())
        print(c.to_line_protocol())

        assert "test,foo=1 bar=2i" == r.to_line_protocol()
        assert "test,foo=1,foobar=3 bar=2i,barfoo=4i" == c.to_line_protocol()


if __name__ == "__main__":
    main()
