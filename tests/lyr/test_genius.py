from lyr.providers import genius

def test_genius():
    query = "ellie goulding your song"
    expected = """It's a little bit funny
This feeling inside
I'm not one of those who can easily hide
I don't have much money
But boy if I did
I'd buy a big house where
We both could live
So excuse me forgetting
But these things I do
See I've forgotten if
They're green or they're blue
Anyway the thing is
What I really mean
Yours are the sweetest eyes I've ever seen
And you can tell everybody
This is your song
It may be quite simple but
Now that it's done
I hope you don't mind, I hope you don't mind
That I put down in words
How wonderful life is now you're in the world
If I was a sculptor
But then again no
Or girl who makes potions in a traveling show
I know it's not much but
It's the best I can do
My gift is my song and
This one's for you
Ohh
And you can tell everybody
This is your song
It may be quite simple but
Now that it's done
I hope you don't mind, I hope you don't mind
That I put down in words
How wonderful life is now you're in the world"""
    actual = genius.lyrics(query)
    assert actual == expected