---
title: typescript sample
tags: js
date: 2019-02-28
---

### 安装 typescript

```js
npm install -g typescript
// 使用 tsc -v 查看安装的版本
```

### 初始化环境 npm

`npm init` 初始化 package.json,并安装 lodash, request 和其 typescript 声明文件 `@types/lodash, @types/request`
编写启动脚本 `"start": "tsc && node out/index.js"`

```json
{
  "name": "github-report",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "start": "tsc && node out/index.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "lodash": "^4.17.15",
    "request": "^2.88.0"
  },
  "devDependencies": {
    "@types/lodash": "^4.14.137",
    "@types/request": "^2.48.2"
  }
}
```

### 初始化 typescript 环境

`tsc --init` 初始化 tsconfig.json

src typescript 源文件目录，out 编译后的 es5 js 文件

```json
{
  "compilerOptions": {
    /* Basic Options */
    // "incremental": true,                   /* Enable incremental compilation */
    "target": "es5",
    /* Specify ECMAScript target version: 'ES3' (default), 'ES5', 'ES2015', 'ES2016', 'ES2017', 'ES2018', 'ES2019' or 'ESNEXT'. */
    "module": "commonjs",
    /* Specify module code generation: 'none', 'commonjs', 'amd', 'system', 'umd', 'es2015', or 'ESNext'. */
    // "lib": [],                             /* Specify library files to be included in the compilation. */
    // "allowJs": true,                       /* Allow javascript files to be compiled. */
    // "checkJs": true,                       /* Report errors in .js files. */
    // "jsx": "preserve",                     /* Specify JSX code generation: 'preserve', 'react-native', or 'react'. */
    // "declaration": true,                   /* Generates corresponding '.d.ts' file. */
    // "declarationMap": true,                /* Generates a sourcemap for each corresponding '.d.ts' file. */
    // "sourceMap": true,                     /* Generates corresponding '.map' file. */
    // "outFile": "./",                       /* Concatenate and emit output to single file. */
    "outDir": "./out",
    /* Redirect output structure to the directory. */
    "rootDir": "./src",
    /* Specify the root directory of input files. Use to control the output directory structure with --outDir. */
    // "composite": true,                     /* Enable project compilation */
    // "tsBuildInfoFile": "./",               /* Specify file to store incremental compilation information */
    // "removeComments": true,                /* Do not emit comments to output. */
    // "noEmit": true,                        /* Do not emit outputs. */
    // "importHelpers": true,                 /* Import emit helpers from 'tslib'. */
    // "downlevelIteration": true,            /* Provide full support for iterables in 'for-of', spread, and destructuring when targeting 'ES5' or 'ES3'. */
    // "isolatedModules": true,               /* Transpile each file as a separate module (similar to 'ts.transpileModule'). */

    /* Strict Type-Checking Options */
    "strict": true,
    /* Enable all strict type-checking options. */
    // "noImplicitAny": true,                 /* Raise error on expressions and declarations with an implied 'any' type. */
    // "strictNullChecks": true,              /* Enable strict null checks. */
    // "strictFunctionTypes": true,           /* Enable strict checking of function types. */
    // "strictBindCallApply": true,           /* Enable strict 'bind', 'call', and 'apply' methods on functions. */
    "strictPropertyInitialization": false,
    /* Enable strict checking of property initialization in classes. */
    // "noImplicitThis": true,                /* Raise error on 'this' expressions with an implied 'any' type. */
    // "alwaysStrict": true,                  /* Parse in strict mode and emit "use strict" for each source file. */

    /* Additional Checks */
    // "noUnusedLocals": true,                /* Report errors on unused locals. */
    // "noUnusedParameters": true,            /* Report errors on unused parameters. */
    // "noImplicitReturns": true,             /* Report error when not all code paths in function return a value. */
    // "noFallthroughCasesInSwitch": true,    /* Report errors for fallthrough cases in switch statement. */

    /* Module Resolution Options */
    // "moduleResolution": "node",            /* Specify module resolution strategy: 'node' (Node.js) or 'classic' (TypeScript pre-1.6). */
    // "baseUrl": "./",                       /* Base directory to resolve non-absolute module names. */
    // "paths": {},                           /* A series of entries which re-map imports to lookup locations relative to the 'baseUrl'. */
    // "rootDirs": [],                        /* List of root folders whose combined content represents the structure of the project at runtime. */
    // "typeRoots": [],                       /* List of folders to include type definitions from. */
    // "types": [],                           /* Type declaration files to be included in compilation. */
    // "allowSyntheticDefaultImports": true,  /* Allow default imports from modules with no default export. This does not affect code emit, just typechecking. */
    "esModuleInterop": true /* Enables emit interoperability between CommonJS and ES Modules via creation of namespace objects for all imports. Implies 'allowSyntheticDefaultImports'. */
    // "preserveSymlinks": true,              /* Do not resolve the real path of symlinks. */
    // "allowUmdGlobalAccess": true,          /* Allow accessing UMD globals from modules. */

    /* Source Map Options */
    // "sourceRoot": "",                      /* Specify the location where debugger should locate TypeScript files instead of source locations. */
    // "mapRoot": "",                         /* Specify the location where debugger should locate map files instead of generated locations. */
    // "inlineSourceMap": true,               /* Emit a single file with source maps instead of having a separate file. */
    // "inlineSources": true,                 /* Emit the source alongside the sourcemaps within a single file; requires '--inlineSourceMap' or '--sourceMap' to be set. */

    /* Experimental Options */
    // "experimentalDecorators": true,        /* Enables experimental support for ES7 decorators. */
    // "emitDecoratorMetadata": true,         /* Enables experimental support for emitting type metadata for decorators. */
  }
}
```

### 业务代码

src/index.ts

```ts
import * as _ from 'lodash'
import { GithubApiService } from './GithubApiService'
import { User } from './User'
import { Repo } from './Repo'

let service: GithubApiService = new GithubApiService()

if (process.argv.length < 3) {
  console.log('Please input username!')
} else {
  let username = process.argv[2]
  service.getUserInfo(username, (user: User) => {
    service.getRepos(username, (repos: Repo[]) => {
      let sortedRepos = _.sortBy(repos, [(repo: Repo) => repo.id * -1])
      user.repos = sortedRepos
      console.log(user)
    })
  })
}

// service.getRepos('lhchen74', (repos: Repo[]) => {
//   console.log(repos)
// })
```

src/GithubApiService.ts

```ts
// You would use import * as in either TypeScript or JavaScript when you want access to all of the module exports in a single variable.
import * as request from 'request'
import { User } from './User'
import { Repo } from './Repo'

const options = {
  headers: {
    'User-Agent': 'request'
  }
}

export class GithubApiService {
  getUserInfo(userName: string, callback: (user: User) => any) {
    request.get(`https://api.github.com/users/${userName}`, options, function(
      error: any,
      response: any,
      body: any
    ) {
      let user = new User(JSON.parse(body))
      callback(user)
    })
  }

  getRepos(userName: string, callback: (repo: Repo[]) => any) {
    request.get(
      `https://api.github.com/users/${userName}/repos`,
      options,
      function(error: any, response: any, body: any) {
        let repos: Repo[] = JSON.parse(body).map((repo: any) => new Repo(repo))
        callback(repos)
      }
    )
  }
}
```

src/Repo.ts

```ts
export class Repo {
  id: number
  name: string
  fullName: string
  url: string
  description: string

  constructor(repo: any) {
    this.id = Number(repo.id)
    this.name = repo.name
    this.fullName = repo.full_name
    this.url = repo.url
    this.description = repo.description
  }
}
```

src/User.ts

```ts
import { Repo } from './Repo'

export class User {
  login: string
  fullName: string
  repoCount: string
  followerCount: string
  repos: Repo[] = [] // 直接初始化，不通过构造函数初始化

  constructor(userRes: any) {
    this.login = userRes.login
    this.fullName = userRes.login
    this.repoCount = userRes.public_repos
    this.followerCount = userRes.followers
  }
}
```

### 运行

`npm run start lhchen74`

```json
User {
  repos: [
    Repo {
      id: 208288712,
      name: 'golang-study',
      fullName: 'lhchen74/golang-study',
      url: 'https://api.github.com/repos/lhchen74/golang-study',
      description: null
    },
    Repo {
      id: 207568664,
      name: 'nest-blog',
      fullName: 'lhchen74/nest-blog',
      url: 'https://api.github.com/repos/lhchen74/nest-blog',
      description: 'node nest '
    },
    Repo {
      id: 205557949,
      name: 'jbn',
      fullName: 'lhchen74/jbn',
      url: 'https://api.github.com/repos/lhchen74/jbn',
      description: 'markdown note'
    }]
}
```
