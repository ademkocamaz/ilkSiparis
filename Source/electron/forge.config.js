const { FusesPlugin } = require('@electron-forge/plugin-fuses');
const { FuseV1Options, FuseVersion } = require('@electron/fuses');
const { features } = require('node:process');

module.exports = {
  packagerConfig: {
    asar: true,
    extraResource: [
      '../django/dist/manage/_internal',
      '../django/dist/manage/manage.exe',
      // '../django/dist/manage/dmidecode.exe',
    ],
    icon: './src/img/logo',
  },
  rebuildConfig: {},
  makers: [
    /* {
      name: '@electron-forge/maker-squirrel',
      config: {
        icon: "./src/img/logo.ico",
        setupIcon: "./src/img/logo.ico",
      },
    }, */
    {
      name: '@electron-forge/maker-wix',
      config: {
        //codepage: "1254",
        appUserModelId: "ilkadam.ilksiparis",
        icon: "./src/img/logo.ico",
        arch: "x64",
        extensions: ["WixUIExtension",],
        cultures: "tr-TR",
        language: 1033,
        manufacturer: 'İLKADAM YAZILIM VE BİLİŞİM TEKNOLOJİLERİ',
        //lightSwitches: ["-sval",],
        ui: {
          enabled: true,
          chooseDirectory: true,
        },
        beforeCreate: (msiCreator) => {
          const getTemplate = (name, trimTrailingNewLine) => {
            const content = require("node:fs").readFileSync(require("node:path").join(__dirname, `./src/${name}.xml`), 'utf-8');
            if (trimTrailingNewLine) {
              return content.replace(/[\r\n]+$/g, '');
            } else {
              return content;
            }
          };
          msiCreator.wixTemplate = getTemplate("wix", false)
          //console.log(msiCreator)
        }
      }
    },
    /* {
      name: '@electron-forge/maker-zip',
    }, */
  ],
  plugins: [
    {
      name: '@electron-forge/plugin-auto-unpack-natives',
      config: {},
    },
    // Fuses are used to enable/disable various Electron functionality
    // at package time, before code signing the application
    new FusesPlugin({
      version: FuseVersion.V1,
      [FuseV1Options.RunAsNode]: false,
      [FuseV1Options.EnableCookieEncryption]: true,
      [FuseV1Options.EnableNodeOptionsEnvironmentVariable]: false,
      [FuseV1Options.EnableNodeCliInspectArguments]: false,
      [FuseV1Options.EnableEmbeddedAsarIntegrityValidation]: true,
      [FuseV1Options.OnlyLoadAppFromAsar]: true,
    }),
  ],
  publishers: [
    {
      name: '@electron-forge/publisher-github',
      config: {
        authToken: '',
        repository: {
          owner: 'ademkocamaz',
          name: 'ilkSiparis'
        },
        draft: true,
      }
    }
  ]
};
