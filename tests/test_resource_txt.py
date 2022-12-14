import configparser
import os
import sys

import pytest

@pytest.fixture
def src2_path():
    return os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            os.pardir,
            "src", "New Mobility",
        )
    )


def test_src2_path(src2_path):
    assert os.path.exists(src2_path), (
        f"unable to find {src2_path}\n"
        f"current folder = {os.path.abspath(os.curdir)}"
    )


@pytest.fixture
def resource_path(src2_path):
    return os.path.abspath(
        os.path.join(src2_path, "resource"
        )
    )


def test_resource_path(resource_path):
    assert os.path.exists(resource_path), (
        f"unable to find {resource_path}\n"
        f"current folder = {os.path.abspath(os.curdir)}"
    )


@pytest.fixture
def gain_txt_fname(resource_path):
    return os.path.abspath(
        os.path.join(resource_path, "gain.txt"
        )
    )


def test_gain_txt_fname(gain_txt_fname):
    assert os.path.exists(gain_txt_fname), (
        f"unable to find {gain_txt_fname}\n"
        f"current folder = {os.path.abspath(os.curdir)}"
    )


@pytest.fixture
def rgb_range_txt_fname(resource_path):
    return os.path.abspath(
        os.path.join(resource_path, "rgb_range.txt"
        )
    )


def test_rgb_range_txt_fname(rgb_range_txt_fname):
    assert os.path.exists(rgb_range_txt_fname), (
        f"unable to find {rgb_range_txt_fname}\n"
        f"current folder = {os.path.abspath(os.curdir)}"
    )


def test_read_gain_txt(gain_txt_fname):
    config = configparser.ConfigParser()
    config.read(gain_txt_fname)

    assert "parameter" in config.sections()

    param = config["parameter"]
    keys = ("ky","ka", "kcv","kcl","Vmax","Aymax",)

    for key in keys:
        assert key in param


def test_read_rgb_range_txt_fname(rgb_range_txt_fname):
    config = configparser.ConfigParser()
    config.read(rgb_range_txt_fname)

    assert "range" in config.sections()

    param = config["range"]
    keys = ("r1","r2", "g1","g2","b1","b2",)

    for key in keys:
        assert key in param
