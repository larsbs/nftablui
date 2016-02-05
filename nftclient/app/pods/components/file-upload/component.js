import Ember from 'ember';
import EmberUploader from 'ember-uploader';

export default EmberUploader.FileField.extend({
  url: undefined,
  filesDidChange: function (files) {
    let uploadUrl = this.get('url');

    let uploader = EmberUploader.Uploader.create({
      url: uploadUrl
    });

    if ( ! Ember.isEmpty(files)) {
      uploader.upload(files[0])
        .then((data) => {
          Ember.$.notification('success', 'Copia de seguridad restaurada correctamente.');
        })
        .catch((err) => {
          Ember.$.notification('error', 'Fallo al restaurar la copia de seguridad.');
        });
    }
  }
});
