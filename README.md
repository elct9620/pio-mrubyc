mruby/c for PlatformIO
===

Add `library.json` to mruby/c repository may cause users confused ([PR #65](https://github.com/mrubyc/mrubyc/pull/65)), so I create another repo to sync the release for PlatformIO user.

## Usage

Add `lib_deps` to your `platformio.ini` config.

```ini
;platformio.ini

; ...
lib_deps =
  git@github.com:elct9620/pio-mrubyc.git
```

Start using your mrubyc in your project

```c
// ESP-IDF
#include "mrubyc.h"

#define MEMORY_SIZE (1024*30)
static uint8_t memory_pool[MEMORY_SIZE];

void app_main() {
  mrbc_init(memory_pool, MEMORY_SIZE);

  // ...
}
```
> Currently, this library not approved by PlatformIO so we cannot find it, but you can use git as the dependency.
