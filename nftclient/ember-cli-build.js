/* global require, module */
var EmberApp = require('ember-cli/lib/broccoli/ember-app');
var Funnel = require('broccoli-funnel');

module.exports = function(defaults) {
  var app = new EmberApp(defaults, {
    lessOptions: {
      paths: [
        'bower_components/bootswatch',
        'bower_components/bootstrap/less',
        'bower_components/fontawesome/less',
        'bower_components/bootstrap-select/dist/css'
      ]
    }
  });

  // Import bootstrap js
  app.import('bower_components/bootstrap/dist/js/bootstrap.js');

  // Import bootstrap-select js
  app.import('bower_components/bootstrap-select/dist/js/bootstrap-select.js');

  // Import noty js
  app.import('bower_components/noty/js/noty/packaged/jquery.noty.packaged.js');
  app.import('bower_components/noty/js/noty/themes/bootstrap.js');
  app.import('bower_components/noty/js/noty/themes/relax.js');

  // Import velocity js
  app.import('bower_components/velocity/velocity.js');
  app.import('bower_components/velocity/velocity.ui.js');

  // Import fontawesome fonts
  var fontAwesome = Funnel('bower_components/fontawesome', {
    srcDir: 'fonts',
    destDir: 'fonts'
  });

  return app.toTree([fontAwesome]);
};
