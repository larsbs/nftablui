module.exports = function(app) {
  var express = require('express');
  var statementsRouter = express.Router();

  var STATEMENTS = [
    {
      id: 'ip:ip_lars:filter_lars:1:1',
      match: '8.8.8.8',
      action: 'counter'
    },
    {
      id: 'ip:ip_lars:filter_lars:1:2',
      match: '192.168.1.3',
      action: 'jump filter_lars2'
    },
    {
      id: 'ip:ip_lars:filter_lars:2:1',
      match: '22',
      action: 'counter'
    }
  ];

  statementsRouter.get('/', function(req, res) {
    res.send({
      'statements': STATEMENTS
    });
  });

  statementsRouter.post('/', function(req, res) {
    res.status(201).end();
  });

  statementsRouter.get('/:id', function(req, res) {
    res.send({
      'statement': STATEMENTS.getById(req.params.id)
    });
  });

  statementsRouter.put('/:id', function(req, res) {
    res.send({
      'statements': {
        id: req.params.id
      }
    });
  });

  statementsRouter.delete('/:id', function(req, res) {
    res.status(204).end();
  });

  app.use('/api/statements', statementsRouter);
};
