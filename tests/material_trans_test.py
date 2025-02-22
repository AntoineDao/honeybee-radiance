from honeybee_radiance.modifier.material import Trans


def test_trans():
    tr = Trans('test_trans')
    assert tr.r_reflectance == 0
    assert tr.g_reflectance == 0
    assert tr.b_reflectance == 0
    assert tr.specularity == 0
    assert tr.roughness == 0
    assert tr.transmitted_diff == 0
    assert tr.transmitted_spec == 0
    assert tr.to_radiance(
        minimal=True) == 'void trans test_trans 0 0 7 0.0 0.0 0.0 0.0 0.0 0.0 0.0'


def test_assign_values():
    tr = Trans('test_trans', 0.7, 0.7, 0.7, 0.01, 0, 0.45, 0.01)
    assert tr.r_reflectance == 0.7
    assert tr.g_reflectance == 0.7
    assert tr.b_reflectance == 0.7
    assert tr.specularity == 0.01
    assert tr.roughness == 0.0
    assert tr.transmitted_diff == 0.45
    assert tr.transmitted_spec == 0.01
    assert tr.to_radiance(
        minimal=True) == 'void trans test_trans 0 0 7 0.7 0.7 0.7 0.01 0.0 0.45 0.01'


def test_update_values():
    tr = Trans('test_trans', 0.7, 0.7, 0.7, 0.01, 0, 0.45, 0.01)
    tr.r_reflectance = 0.5
    tr.g_reflectance = 0.4
    tr.b_reflectance = 0.3
    tr.specularity = 0.1
    tr.roughness = 0.02
    tr.transmitted_diff = 0.45
    tr.transmitted_spec = 0.01

    assert tr.r_reflectance == 0.5
    assert tr.g_reflectance == 0.4
    assert tr.b_reflectance == 0.3
    assert tr.specularity == 0.1
    assert tr.roughness == 0.02
    assert tr.transmitted_diff == 0.45
    assert tr.transmitted_spec == 0.01
    assert tr.to_radiance(minimal=True) == \
        'void trans test_trans 0 0 7 0.5 0.4 0.3 0.1 0.02 0.45 0.01'


def test_from_string():
    trans_str = """
    void trans test
        0
        0
        7
            0.7 0.7 0.7
            0.01 0.0 0.45
            0.01
            
    """
    tr = Trans.from_string(trans_str)
    assert tr.identifier == 'test'
    assert tr.r_reflectance == 0.7
    assert tr.g_reflectance == 0.7
    assert tr.b_reflectance == 0.7
    assert tr.specularity == 0.01
    assert tr.roughness == 0.0
    assert tr.transmitted_diff == 0.45
    assert tr.transmitted_spec == 0.01
    assert tr.to_radiance(minimal=True) == ' '.join(trans_str.split())


def test_from_single_value():
    tr = Trans.from_single_reflectance('test', 0.6)
    assert tr.r_reflectance == 0.6
    assert tr.g_reflectance == 0.6
    assert tr.b_reflectance == 0.6
