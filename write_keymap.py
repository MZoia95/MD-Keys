content = open('/Users/adamlangdon/MD-Keys/keyboards/mfkeys/keymaps/default/keymap.c', 'w')
content.write('''#include QMK_KEYBOARD_H

enum custom_keycodes {
    MD_M1 = QK_USER,
    MD_M2, MD_M3, MD_M4, MD_M5, MD_M6,
    MD_M7, MD_M8, MD_M9, MD_M10, MD_M11, MD_M12
};

bool process_record_user(uint16_t keycode, keyrecord_t *record) {
    switch (keycode) {
        case MD_M1:
            if (record->event.pressed) { tap_code(KC_MUTE); }
            return false;
        case MD_M2:
            if (record->event.pressed) { tap_code(KC_VOLD); }
            return false;
        case MD_M3:
            if (record->event.pressed) { tap_code(KC_VOLU); }
            return false;
        case MD_M4:
            if (record->event.pressed) { tap_code(KC_MPRV); }
            return false;
        case MD_M5:
            if (record->event.pressed) { tap_code(KC_MPLY); }
            return false;
        case MD_M6:
            if (record->event.pressed) { tap_code(KC_MNXT); }
            return false;
        case MD_M7:
            if (record->event.pressed) {
                register_code(KC_LGUI);
                register_code(KC_LSFT);
                tap_code(KC_S);
                unregister_code(KC_LSFT);
                unregister_code(KC_LGUI);
            }
            return false;
        case MD_M8:
            if (record->event.pressed) { tap_code(KC_CALC); }
            return false;
        case MD_M9:
            if (record->event.pressed) { tap_code(KC_MAIL); }
            return false;
        case MD_M10:
            if (record->event.pressed) {
                register_code(KC_LCTL);
                register_code(KC_LSFT);
                tap_code(KC_ESC);
                unregister_code(KC_LSFT);
                unregister_code(KC_LCTL);
            }
            return false;
        case MD_M11:
            if (record->event.pressed) { tap_code(KC_BRID); }
            return false;
        case MD_M12:
            if (record->event.pressed) { tap_code(KC_BRIU); }
            return false;
    }
    return true;
}

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT(
        MD_M1,   MD_M2,   MD_M3,   MD_M4,   MD_M5,   MD_M6,   MD_M7,   MD_M8,   MD_M9,   MD_M10,  MD_M11,  MD_M12,
        KC_ESC,  KC_F1,   KC_F2,   KC_F3,   KC_F4,   KC_F5,   KC_F6,   KC_F7,   KC_F8,   KC_F9,   KC_F10,  KC_F11,  KC_F12,  KC_PSCR, KC_SCRL, KC_PAUS,
        KC_GRV,  KC_1,    KC_2,    KC_3,    KC_4,    KC_5,    KC_6,    KC_7,    KC_8,    KC_9,    KC_0,    KC_MINS, KC_EQL,  KC_BSPC, KC_INS,
        KC_TAB,  KC_Q,    KC_W,    KC_E,    KC_R,    KC_T,    KC_Y,    KC_U,    KC_I,    KC_O,    KC_P,    KC_LBRC, KC_RBRC,
        KC_LSFT, KC_Z,    KC_X,    KC_C,    KC_V,    KC_B,    KC_N,    KC_M,    KC_COMM, KC_DOT,  KC_SLSH, KC_RSFT, KC_UP,
        KC_LCTL, KC_LGUI, KC_LALT, KC_SPC,  KC_RALT, KC_RGUI, KC_APP,  KC_RCTL, KC_LEFT, KC_DOWN, KC_RGHT
    ),
    [1] = LAYOUT(
        MD_M1,   MD_M2,   MD_M3,   MD_M4,   MD_M5,   MD_M6,   MD_M7,   MD_M8,   MD_M9,   MD_M10,  MD_M11,  MD_M12,
        KC_ESC,  KC_F1,   KC_F2,   KC_F3,   KC_F4,   KC_F5,   KC_F6,   KC_F7,   KC_F8,   KC_F9,   KC_F10,  KC_F11,  KC_F12,  KC_PSCR, KC_SCRL, KC_PAUS,
        KC_GRV,  KC_1,    KC_2,    KC_3,    KC_4,    KC_5,    KC_6,    KC_7,    KC_8,    KC_9,    KC_0,    KC_MINS, KC_EQL,  KC_BSPC, KC_INS,
        KC_TAB,  KC_Q,    KC_W,    KC_E,    KC_R,    KC_T,    KC_Y,    KC_U,    KC_I,    KC_O,    KC_P,    KC_LBRC, KC_RBRC,
        KC_LSFT, KC_Z,    KC_X,    KC_C,    KC_V,    KC_B,    KC_N,    KC_M,    KC_COMM, KC_DOT,  KC_SLSH, KC_RSFT, KC_UP,
        KC_LCTL, KC_LGUI, KC_LALT, KC_SPC,  KC_RALT, KC_RGUI, KC_APP,  KC_RCTL, KC_LEFT, KC_DOWN, KC_RGHT
    ),
    [2] = LAYOUT(
        MD_M1,   MD_M2,   MD_M3,   MD_M4,   MD_M5,   MD_M6,   MD_M7,   MD_M8,   MD_M9,   MD_M10,  MD_M11,  MD_M12,
        KC_ESC,  KC_F1,   KC_F2,   KC_F3,   KC_F4,   KC_F5,   KC_F6,   KC_F7,   KC_F8,   KC_F9,   KC_F10,  KC_F11,  KC_F12,  KC_PSCR, KC_SCRL, KC_PAUS,
        KC_GRV,  KC_1,    KC_2,    KC_3,    KC_4,    KC_5,    KC_6,    KC_7,    KC_8,    KC_9,    KC_0,    KC_MINS, KC_EQL,  KC_BSPC, KC_INS,
        KC_TAB,  KC_Q,    KC_W,    KC_E,    KC_R,    KC_T,    KC_Y,    KC_U,    KC_I,    KC_O,    KC_P,    KC_LBRC, KC_RBRC,
        KC_LSFT, KC_Z,    KC_X,    KC_C,    KC_V,    KC_B,    KC_N,    KC_M,    KC_COMM, KC_DOT,  KC_SLSH, KC_RSFT, KC_UP,
        KC_LCTL, KC_LGUI, KC_LALT, KC_SPC,  KC_RALT, KC_RGUI, KC_APP,  KC_RCTL, KC_LEFT, KC_DOWN, KC_RGHT
    ),
    [3] = LAYOUT(
        MD_M1,   MD_M2,   MD_M3,   MD_M4,   MD_M5,   MD_M6,   MD_M7,   MD_M8,   MD_M9,   MD_M10,  MD_M11,  MD_M12,
        KC_ESC,  KC_F1,   KC_F2,   KC_F3,   KC_F4,   KC_F5,   KC_F6,   KC_F7,   KC_F8,   KC_F9,   KC_F10,  KC_F11,  KC_F12,  KC_PSCR, KC_SCRL, KC_PAUS,
        KC_GRV,  KC_1,    KC_2,    KC_3,    KC_4,    KC_5,    KC_6,    KC_7,    KC_8,    KC_9,    KC_0,    KC_MINS, KC_EQL,  KC_BSPC, KC_INS,
        KC_TAB,  KC_Q,    KC_W,    KC_E,    KC_R,    KC_T,    KC_Y,    KC_U,    KC_I,    KC_O,    KC_P,    KC_LBRC, KC_RBRC,
        KC_LSFT, KC_Z,    KC_X,    KC_C,    KC_V,    KC_B,    KC_N,    KC_M,    KC_COMM, KC_DOT,  KC_SLSH, KC_RSFT, KC_UP,
        KC_LCTL, KC_LGUI, KC_LALT, KC_SPC,  KC_RALT, KC_RGUI, KC_APP,  KC_RCTL, KC_LEFT, KC_DOWN, KC_RGHT
    )
};
''')
content.close()
print('keymap.c written successfully!')
