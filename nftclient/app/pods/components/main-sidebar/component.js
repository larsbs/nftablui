import Ember from 'ember';

function collapseToggle() {
  var clicked = Ember.$(this);
  var collapsible = clicked.parent().find('.nav-collapsible');
  var chevron = clicked.find('.fa-chevron-left');

  chevron.toggleClass('open');
  if (chevron.hasClass('open')) {
    chevron.velocity({ rotateZ: '-90deg' });
    collapsible.velocity('slideDown', { duration: 400 });
  }
  else {
    chevron.velocity({ rotateZ: '0deg' });
    collapsible.velocity('slideUp', { duration: 400 });
  }

}

export default Ember.Component.extend({
  tagName: 'div',
  classNames: ['main-sidebar'],

  didInsertElement: function () {
    this.$('section.collapsible > .section-header').click(collapseToggle);
  }
});
