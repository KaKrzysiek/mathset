/*
 * Copyright (c) 2023 Krzysztof Karczewski
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at https://mozilla.org/MPL/2.0/.
 */

// Source code copied to clipboard after button clicked
const SOURCE_CODE = [
    "from mathset import MathSet\nA = MathSet({1, 2, 3})\nprint(A)\nB = MathSet()\nprint(B)\nC = MathSet([A, B])\nprint(C)",
    "from mathset import MathSet\nA = MathSet()\nprint(A.is_empty())",
    "from mathset import MathSet\nA = MathSet({1, 2, 3})\nB = MathSet({2, 3})\nC = MathSet({3, 4})\nprint(B.is_subset(A))\nprint(C.is_subset(A))",
    "from mathset import MathSet\nA = MathSet({1, 2, 3, 4})\nB = MathSet({2, 3, 4, 5})\nC = MathSet({2, 3})\nD = MathSet([A, B, C])\nprint(D.is_family_of_sets(), B.is_family_of_sets())\nprint(D.family_union())\nprint(D.family_intersection())",
    "from mathset import MathSet\nA = MathSet({1, 2, 3})\nB = A.power_set()\nprint(B)",
    "from mathset import MathSet\nA = MathSet({0, 1, 2, 3, 4})\nB = MathSet({-4, -3, -2, -1, 0, 1, 2, 3, 4})\nC = A.cartesian_product(B)\nR = MathSet([(a, b) for (a, b) in C if a == abs(b)])\nprint(R)\nprint(R.domain())\nprint(R.range())",
    "from mathset import MathSet\nA = MathSet(range(0, 101))\nB = A.cartesian_product(A)\nf = MathSet([(x, y) for (x, y) in B if y == x**2])\nprint(f.is_function())\nprint(f.image({1, 2, 3, 4}))\nprint(f.value(7))\ng = f.restriction({0, 1, 2})\nprint(g)",
    "from mathset import MathSet\nA = MathSet(range(1, 13))\nB = A.cartesian_product(A)\nf = MathSet([(x, y) for (x, y) in B if x*y % 13 == 1])\nprint(f.is_injection(A, A))\nprint(f.is_surjection(A, A))\nprint(f.is_bijection(A, A))\ng = f.inverse()\nprint(g.value(7))",
    "from mathset import MathSet\nA = MathSet(range(-50, 51))\nB = A.cartesian_product(A)\nR = MathSet([(a, b) for (a, b) in B if a % 10 == b % 10])\nprint(R.is_reflective(A))\nprint(R.is_symmetric(A))\nprint(R.is_transitive(A))\nprint(R.is_equivalence(A))\nprint(R.equivalence_class(7))",
    "from mathset import MathSet\nA = MathSet(range(-10, 11))\nB = A.cartesian_product(A)\nR1 = MathSet([(a, b) for (a, b) in B if a < b])\nR2 = MathSet([(a, b) for (a, b) in B if a <= b])\nprint(R1.is_strict_linear_ordering(A))\nprint(R2.is_strict_linear_ordering(A))",
    "from mathset import MathSet\nA = MathSet({0, 1, 2, 3, 4, 5})\nB = MathSet([{0, 2, 4}, {1, 3, 5}])\nC = A.power_set()\nprint(B.is_partition(A))\nprint(C.is_partition(A))",
    "from mathset import MathSet\n\ndef natural_number(n):\n\tif n == 0:\n\t\treturn MathSet()\n\tprev = natural_number(n - 1)\n\tsingleton = MathSet([prev])\n\treturn MathSet(prev.union(singleton))\n\nfor i in range(5):\n\tprint(natural_number(i))",
    "from mathset import MathSet\n\na = lambda b, c : \"R is \" + c if b else \"R is not \" + c\n\nA = MathSet({0, 1, 2})\nB = A.power_set()\nC = B.cartesian_product(B)\nR = MathSet([(a, b) for (a, b) in C if MathSet(a).is_subset(b)])\nprint(a(R.is_reflective(B), \"reflective\"))\nprint(a(R.is_symmetric(B), \"symmetric\"))\nprint(a(R.is_transitive(B), \"transitive\"))\nprint(a(R.is_total(B), \"total\"))\nprint(a(R.is_antisymmetric(B), \"antisymmetric\"))"
];

// Makes it harder for spam bots to read email
const ENCODED_EMAIL = 'a2Frcnp5c2llazEzQGdtYWlsLmNvbQ==';

// Stores current theme
var lightThemeOn = true;

//Changes website theme after clicking the button. User can choose between light and dark.
function changeTheme() {
    document.documentElement.className = (lightThemeOn ? "dark" : "light");
    document.getElementById("change-theme-button").title = (lightThemeOn ? "Enable light mode" : "Enable dark mode");
    document.getElementById("moon-picture").hidden = lightThemeOn;
    document.getElementById("sun-picture").hidden = !lightThemeOn;
    lightThemeOn = !lightThemeOn;
}

// Checks if access to clipboard is granted
function checkClipboardPermissions() {
    if(navigator.clipboard === undefined) {
        return false;
    }
    return navigator.permissions.query({ name : "write-on-clipboard" }).then((result) => {
        if (result.state == "granted" || result.state == "prompt") {
            return true;
        } else {
            return false;
        }
    });
}

// Copies source code to clipboard
function copyToClipboard(sourceCodeNo) {
    // No access to clipboard
    if(!checkClipboardPermissions()) {
        return;
    }
    navigator.clipboard.writeText(SOURCE_CODE[sourceCodeNo - 1]);
    button = document.getElementById("copy-button-" + sourceCodeNo.toString());
    // Change style and inform about code copied
    button.style.borderColor = "#1bc51e";
    button.innerHTML = "copied";
    button.style.color = "#1bc51e";
    // Freeze for 1.5 seconds
    setTimeout(function(){
        button.style.borderColor = "var(--copy-button-border-color)";
        button.innerHTML = "copy";
        button.style.color = "var(--text-color)";
    }, 1500);
}

// Initialise function. If not called, all the
// javaScript functionalities will stay hidden.
function init() {
    document.getElementById('change-theme-button').hidden = false;
    document.getElementById('contact').title = "Contact me";
    document.getElementById('contact').href = 'mailto:' + atob(ENCODED_EMAIL);
    changeTheme();
    if(checkClipboardPermissions()) {
        for(let i = 1; i <= SOURCE_CODE.length; i++) {
            document.getElementById("copy-button-" + i.toString()).hidden = false;
        }
    }
}
