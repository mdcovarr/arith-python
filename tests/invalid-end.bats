load harness

@test "invalid-end-1" {
  check '2 + 3 -' 'Error: Invalid way to end expression'
}

@test "invalid-end-2" {
  check '3 + 92 ++' 'Error: Invalid way to end expression'
}

@test "invalid-end-3" {
  check '1 + 0 + *' 'Error: Invalid way to end expression'
}

@test "invalid-end-4" {
  check '-1 + -3*****' 'Error: Invalid way to end expression'
}

@test "invalid-end-multiple-1" {
  check '99 + 3 + 12 + 2--' 'Error: Invalid way to end expression'
}

@test "invalid-end-multiple-2" {
  check '2 + 3 + 4 + -1+-*+-*' 'Error: Invalid way to end expression'
}

@test "invalid-end-multiple-3" {
  check '-1 + -2 + 3+' 'Error: Invalid way to end expression'
}
