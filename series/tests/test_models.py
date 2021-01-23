import pytest
from series.models import MediaType, Series


@pytest.fixture
def series():
    return Series(
        title="Strike Witches",
        media=MediaType.CARTOON,
    )


def test_series_webnovel(series):
    series.media = MediaType.WEB_NOVEL

    assert series.title == "Strike Witches"
    assert series.media == "Web Novel"


def test_series_lightnovel(series):
    series.media = MediaType.LIGHT_NOVEL

    assert series.media == "Light Novel"


def test_series_comic(series):
    series.media = MediaType.COMIC

    assert series.media == "Comic"


def test_series_cartoon(series):
    series.media = MediaType.CARTOON

    assert series.media == "Cartoon"


def test_series_from_japan(series):
    series.origin = "JP"

    assert series.origin.name == "Japan"


def test_series_media_l10n_japanese_comic(series):
    series.origin = "JP"
    series.media = MediaType.COMIC

    assert series.origin.name == "Japan"
    assert series.media_l10n == "Manga"
    assert series.__str__() == "Strike Witches (Manga)"


def test_series_media_l10n_japanese_cartoon(series):
    series.origin = "JP"
    series.media = MediaType.CARTOON

    assert series.media_l10n == "Anime"
    assert series.__str__() == "Strike Witches (Anime)"


def test_series_media_l10n_korean_comic(series):
    series.origin = "KR"
    series.media = MediaType.COMIC

    assert series.media_l10n == "Manhwa"


def test_series_media_l10n_no_origin_cartoon(series):
    series.media = MediaType.CARTOON

    assert series.media_l10n == "Cartoon"
