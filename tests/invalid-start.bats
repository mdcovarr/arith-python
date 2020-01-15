load harness

@test "invalid-start-1" {
  check '* * 2 - 3' 'Error: Invalid way to start expression'
}

@test "invalid-start-2" {
  check '--42 + 92' 'Error: Invalid way to start expression'
}

@test "invalid-start-3" {
  check '+ + 1 - 0' 'Error: Invalid way to start expression'
}

@test "invalid-start-4" {
  check '- -1 - -3' 'Error: Invalid way to start expression'
}

@test "invalid-start-multiple-1" {
  check '*99 - 3 - 12 - 2' 'Error: Invalid way to start expression'
}

@test "invalid-start-multiple-2" {
  check '******2 + 3 + 4 - 1' 'Error: Invalid way to start expression'
}

@test "invalid-start-multiple-3" {
  check '+*-1 - 2 - 3' 'Error: Invalid way to start expression'
}
