load harness

@test "subtraction-1" {
  check '2 - 3' '-1'
}

@test "subtraction-2" {
  check '-42 + 92' '50'
}

@test "subtraction-3" {
  check '1 - 0' '1'
}

@test "subtraction-4" {
  check '-1 - -3' '2'
}

@test "subtraction-multiple-1" {
  check '99 - 3 - 12 - 2' '82'
}

@test "subtraction-multiple-2" {
  check '2 + 3 + 4 - 1' '8'
}

@test "subtraction-multiple-3" {
  check '-1 - 2 - 3' '-6'
}
