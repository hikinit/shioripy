from series.models import MediaType, Series


def test_create_series_webnovel():
    series = Series(
        title="The Novel's Extra",
        media=MediaType.WEB_NOVEL,
    )

    assert series.title == "The Novel's Extra"
    assert series.media == "Web Novel"
    assert series.__str__() == "The Novel's Extra (Web Novel)"


def test_create_series_lightnovel():
    series = Series(
        title="Infinite Dendrogram",
        media=MediaType.LIGHT_NOVEL,
    )

    assert series.title == "Infinite Dendrogram"
    assert series.media == "Light Novel"
    assert series.__str__() == "Infinite Dendrogram (Light Novel)"


def test_create_series_comic():
    series = Series(
        title="Jungle Juice",
        media=MediaType.COMIC,
    )

    assert series.title == "Jungle Juice"
    assert series.media == "Comic"
    assert series.__str__() == "Jungle Juice (Comic)"


def test_create_series_cartoon():
    series = Series(
        title="Puella Magi Madoka Magica",
        media=MediaType.CARTOON,
    )

    assert series.title == "Puella Magi Madoka Magica"
    assert series.media == "Cartoon"
    assert series.__str__() == "Puella Magi Madoka Magica (Cartoon)"


def test_series_from_japan():
    series = Series(origin="JP")

    assert series.origin.name == "Japan"


def test_series_media_l10n_japanese_comic():
    series = Series(media=MediaType.COMIC, origin="JP")

    assert series.origin.name == "Japan"
    assert series.media_l10n == "Manga"


def test_series_media_l10n_japanese_cartoon():
    series = Series(media=MediaType.CARTOON, origin="JP")

    assert series.media_l10n == "Anime"


def test_series_media_l10n_korean_comic():
    series = Series(media=MediaType.COMIC, origin="KR")

    assert series.media_l10n == "Manhwa"


def test_series_media_l10n_no_origin_cartoon():
    series = Series(media=MediaType.CARTOON)

    assert series.media_l10n == "Cartoon"
