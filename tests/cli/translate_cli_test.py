"""Test cli translate module."""
import os
from click.testing import CliRunner

from ladybug.futil import nukedir

from honeybee_radiance.cli.translate import model_to_rad_folder, model_to_rad, \
    modifier_to_rad, modifier_from_rad, model_radiant_enclosure_info


def test_model_to_rad_folder():
    runner = CliRunner()
    input_hb_model = './tests/assets/model/model_radiance_dynamic_states.hbjson'
    output_hb_model = './tests/assets/model/model'

    result = runner.invoke(model_to_rad_folder, [input_hb_model])
    assert result.exit_code == 0
    assert os.path.isdir(output_hb_model)
    nukedir(output_hb_model, True)


def test_model_to_rad_folder_grid_filter():
    runner = CliRunner()
    input_hb_model = './tests/assets/model/sample_room_with_grid_group.hbjson'
    output_hb_model = './tests/assets/temp/model'

    result = runner.invoke(
        model_to_rad_folder,
        [input_hb_model, '--folder', output_hb_model, '-g', '?pertures/*']
    )
    assert result.exit_code == 0
    assert os.path.isdir(os.path.join(output_hb_model, 'model'))
    assert os.path.isdir(os.path.join(output_hb_model, 'model', 'grid', 'apertures'))
    assert not os.path.isdir(
        os.path.join(output_hb_model, 'model', 'grid', 'occ_regions'))

    nukedir(output_hb_model, True)


def test_model_to_rad():
    runner = CliRunner()
    input_hb_model = './tests/assets/model/model_complete_multiroom_radiance.hbjson'

    result = runner.invoke(model_to_rad, [input_hb_model])
    assert result.exit_code == 0

    output_hb_model = './tests/assets/model/model_complete_multiroom_radiance.rad'
    result = runner.invoke(model_to_rad, [input_hb_model, '--output-file', output_hb_model])
    assert result.exit_code == 0
    assert os.path.isfile(output_hb_model)
    os.remove(output_hb_model)


def test_model_radiant_enclosure_info():
    runner = CliRunner()
    input_hb_model = './tests/assets/model/two_rooms.hbjson'
    output_enclosure_folder = './tests/assets/model/enclosure'

    result = runner.invoke(model_radiant_enclosure_info, [input_hb_model])
    assert result.exit_code == 0
    assert os.path.isdir(output_enclosure_folder)
    nukedir(output_enclosure_folder, True)


def test_modifier_to_from_rad():
    runner = CliRunner()
    input_hb_mod = './tests/assets/modifier/modifier_plastic_generic_wall.json'
    output_hb_rad = './tests/assets/modifier/modifier_plastic_generic_wall.rad'

    result = runner.invoke(modifier_to_rad, [input_hb_mod, '--output-file', output_hb_rad])
    assert result.exit_code == 0
    assert os.path.isfile(output_hb_rad)

    result = runner.invoke(
        modifier_from_rad, [output_hb_rad])
    assert result.exit_code == 0

    os.remove(output_hb_rad)


def test_modifier_to_from_rad_trans():
    runner = CliRunner()
    input_hb_mod = './tests/assets/modifier/modifier_trans_tree_foliage.json'
    output_hb_rad = './tests/assets/modifier/modifier_trans_tree_foliage.rad'

    result = runner.invoke(modifier_to_rad, [input_hb_mod, '--output-file', output_hb_rad])
    assert result.exit_code == 0
    assert os.path.isfile(output_hb_rad)

    result = runner.invoke(
        modifier_from_rad, [output_hb_rad])
    assert result.exit_code == 0

    os.remove(output_hb_rad)
