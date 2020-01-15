load harness

@test "invalid-operators-1" {
  check '2 + + 3 * 4' 'Error: Invalid operator sequences'
}

@test "invalid-operators-2" {
  check '-2 + 3 * - -4 + 6 * 2 * 0' 'Error: Invalid operator sequences'
}

@test "invalid-operators-3" {
  check '3 * * 8 + + 9 * 10' 'Error: Invalid operator sequences'
}
