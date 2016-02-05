module.exports = function(app) {
  var express = require('express');
  var rulesRouter = express.Router();

  var RULES = [
    {
      id: 'ip:ip_lars:filter_lars:1',
      handle: '1',
      position: '1',
      expression: 'ip',
      key: 'daddr',
      statements: [
        {
          match: '8.8.8.8',
          action: 'counter'
        },
        {
          match: '192.168.1.3',
          action: 'jump filter_lars2'
        }
      ]
    },
    {
      id: 'ip:ip_lars:filter_lars:2',
      handle: '2',
      position: '2',
      expression: 'tcp',
      key: 'dport',
      statements: [
        {
          match: '22',
          action: 'counter'
        }
      ]
    },
    {
      id: 'ip:ip_lars:filter_lars:3',
      handle: '3',
      position: '3',
      expression: 'ip',
      key: 'saddr',
      statements: [
        {
          set: '\@qwer',
          action: 'counter'
        }
      ]
    },
    {
      id: 'ip:ip_lars:filter_lars:4',
      handle: '4',
      position: '4',
      expression: 'ip',
      key: 'saddr',
      statements: [
        {
          dictionary: 'vmap \@mydict'
        }
      ]
    }
  ];

  rulesRouter.get('/', function(req, res) {
    res.send({
      'rules': RULES
    });
  });

  rulesRouter.post('/', function(req, res) {
    res.status(201);
    var rule = req.body.rule;
    rule.handle = 5;
    rule.id = rule.chain.id + ':'  + rule.handle;
    res.send({
      'rule': rule
    });
  });

  rulesRouter.get('/:id', function(req, res) {
    res.send({
      'rule': RULES.getById(req.params.id)
    });
  });

  rulesRouter.put('/:id', function(req, res) {
    res.send({
      'rules': {
        id: req.params.id
      }
    });
  });

  rulesRouter.delete('/:id', function(req, res) {
    res.status(204).end();
  });

  app.use('/api/rules', rulesRouter);
};
