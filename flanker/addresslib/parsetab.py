
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'mailbox_or_urlFWSP AT DOT COMMA SEMICOLON LANGLE RANGLE ATOM DOT_ATOM LBRACKET RBRACKET DTEXT DQUOTE QTEXT QPAIR LPAREN RPAREN CTEXT URLmailbox_or_url_list : mailbox_or_url_list delim mailbox_or_url\n                           | mailbox_or_url_list delim\n                           | mailbox_or_urldelim : delim fwsp COMMA\n             | delim fwsp SEMICOLON\n             | COMMA\n             | SEMICOLONmailbox_or_url : mailbox\n                      | urlurl : ofwsp URL ofwspmailbox : addr_spec\n               | angle_addr\n               | name_addrname_addr : ofwsp phrase angle_addrangle_addr : ofwsp LANGLE addr_spec RANGLE ofwspaddr_spec : ofwsp local_part AT domain ofwsplocal_part : DOT_ATOM\n                  | ATOM\n                  | quoted_stringdomain : DOT_ATOM\n              | ATOM\n              | domain_literalquoted_string : DQUOTE quoted_string_text DQUOTE\n                     | DQUOTE DQUOTEquoted_string_text : quoted_string_text QTEXT\n                          | quoted_string_text QPAIR\n                          | quoted_string_text fwsp\n                          | QTEXT\n                          | QPAIR\n                          | fwspdomain_literal : LBRACKET domain_literal_text RBRACKET\n                      | LBRACKET RBRACKETdomain_literal_text : domain_literal_text DTEXT\n                           | domain_literal_text fwsp\n                           | DTEXT\n                           | fwspcomment : LPAREN comment_text RPAREN\n               | LPAREN RPARENcomment_text : comment_text CTEXT\n                    | comment_text fwsp\n                    | CTEXT\n                    | fwspphrase : phrase fwsp ATOM\n              | phrase fwsp DOT_ATOM\n              | phrase fwsp DOT\n              | phrase fwsp quoted_string\n              | phrase ATOM\n              | phrase DOT_ATOM\n              | phrase DOT\n              | phrase quoted_string\n              | ATOM\n              | DOT_ATOM\n              | DOT\n              | quoted_stringofwsp : fwsp comment fwsp\n             | fwsp comment\n             | comment fwsp\n             | comment\n             | fwsp\n             |fwsp : FWSP'
    
_lr_action_items = {'FWSP':([0,2,7,11,12,14,15,17,18,19,20,21,22,23,24,25,26,32,33,34,35,36,40,41,42,43,44,45,46,50,51,52,53,54,55,56,57,58,59,60,61,62,63,66,67,68,69,70,71,72,],[7,7,-61,7,7,7,7,-51,7,-52,7,-54,-53,-42,7,-38,-41,-30,-29,-28,-24,7,-48,-47,-50,-49,-40,-37,-39,7,7,7,-20,-21,-22,-27,-26,-25,-23,-44,-43,-46,-45,-36,-35,7,-32,-34,-33,-31,]),'LANGLE':([0,1,2,4,7,12,13,17,19,20,21,22,25,27,35,37,38,40,41,42,43,45,59,60,61,62,63,],[-60,-59,-58,14,-61,-56,-57,-51,-52,-60,-54,-53,-38,-55,-24,-59,14,-48,-47,-50,-49,-37,-23,-44,-43,-46,-45,]),'QPAIR':([7,18,32,33,34,36,56,57,58,],[-61,33,-30,-29,-28,57,-27,-26,-25,]),'URL':([0,1,2,4,7,12,13,25,27,45,],[-60,-59,-58,15,-61,-56,-57,-38,-55,-37,]),'QTEXT':([7,18,32,33,34,36,56,57,58,],[-61,34,-30,-29,-28,58,-27,-26,-25,]),'DTEXT':([7,52,66,67,68,70,71,],[-61,67,-36,-35,71,-34,-33,]),'DQUOTE':([0,1,2,4,7,12,13,14,17,18,19,20,21,22,25,27,28,32,33,34,35,36,37,40,41,42,43,45,56,57,58,59,60,61,62,63,],[-60,-59,-58,18,-61,-56,-57,-60,-51,35,-52,18,-54,-53,-38,-55,18,-30,-29,-28,-24,59,18,-48,-47,-50,-49,-37,-27,-26,-25,-23,-44,-43,-46,-45,]),'LBRACKET':([31,],[52,]),'DOT_ATOM':([0,1,2,4,7,12,13,14,17,19,20,21,22,25,27,28,31,35,37,40,41,42,43,45,59,60,61,62,63,],[-60,-59,-58,19,-61,-56,-57,-60,-51,-52,40,-54,-53,-38,-55,47,53,-24,60,-48,-47,-50,-49,-37,-23,-44,-43,-46,-45,]),'RPAREN':([7,11,23,24,26,44,46,],[-61,25,-42,45,-41,-40,-39,]),'AT':([16,17,19,21,35,47,48,49,59,],[31,-18,-17,-19,-24,-17,-18,-19,-23,]),'LPAREN':([0,1,7,14,15,17,19,20,21,22,35,37,40,41,42,43,50,51,53,54,55,59,60,61,62,63,69,72,],[11,11,-61,11,11,-51,-52,11,-54,-53,-24,11,-48,-47,-50,-49,11,11,-20,-21,-22,-23,-44,-43,-46,-45,-32,-31,]),'ATOM':([0,1,2,4,7,12,13,14,17,19,20,21,22,25,27,28,31,35,37,40,41,42,43,45,59,60,61,62,63,],[-60,-59,-58,17,-61,-56,-57,-60,-51,-52,41,-54,-53,-38,-55,48,54,-24,61,-48,-47,-50,-49,-37,-23,-44,-43,-46,-45,]),'RANGLE':([1,2,7,12,13,25,27,29,45,51,53,54,55,65,69,72,],[-59,-58,-61,-56,-57,-38,-55,50,-37,-60,-20,-21,-22,-16,-32,-31,]),'RBRACKET':([7,52,66,67,68,70,71,],[-61,69,-36,-35,72,-34,-33,]),'CTEXT':([7,11,23,24,26,44,46,],[-61,26,-42,46,-41,-40,-39,]),'DOT':([0,1,2,4,7,12,13,17,19,20,21,22,25,27,35,37,40,41,42,43,45,59,60,61,62,63,],[-60,-59,-58,22,-61,-56,-57,-51,-52,43,-54,-53,-38,-55,-24,63,-48,-47,-50,-49,-37,-23,-44,-43,-46,-45,]),'$end':([1,2,3,5,6,7,8,9,10,12,13,15,25,27,30,39,45,50,51,53,54,55,64,65,69,72,],[-59,-58,-13,-12,0,-61,-8,-9,-11,-56,-57,-60,-38,-55,-10,-14,-37,-60,-60,-20,-21,-22,-15,-16,-32,-31,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'fwsp':([0,2,11,12,14,15,18,20,24,36,50,51,52,68,],[1,13,23,27,1,1,32,37,44,56,1,1,66,70,]),'comment':([0,1,14,15,20,37,50,51,],[2,12,2,2,2,12,2,2,]),'domain':([31,],[51,]),'comment_text':([11,],[24,]),'name_addr':([0,],[3,]),'ofwsp':([0,14,15,20,50,51,],[4,28,30,38,64,65,]),'angle_addr':([0,20,],[5,39,]),'mailbox_or_url':([0,],[6,]),'local_part':([4,28,],[16,16,]),'domain_literal_text':([52,],[68,]),'mailbox':([0,],[8,]),'quoted_string_text':([18,],[36,]),'url':([0,],[9,]),'addr_spec':([0,14,],[10,29,]),'phrase':([4,],[20,]),'quoted_string':([4,20,28,37,],[21,42,49,62,]),'domain_literal':([31,],[55,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> mailbox_or_url","S'",1,None,None,None),
  ('mailbox_or_url_list -> mailbox_or_url_list delim mailbox_or_url','mailbox_or_url_list',3,'p_expression_mailbox_or_url_list','parser.py',18),
  ('mailbox_or_url_list -> mailbox_or_url_list delim','mailbox_or_url_list',2,'p_expression_mailbox_or_url_list','parser.py',19),
  ('mailbox_or_url_list -> mailbox_or_url','mailbox_or_url_list',1,'p_expression_mailbox_or_url_list','parser.py',20),
  ('delim -> delim fwsp COMMA','delim',3,'p_delim','parser.py',29),
  ('delim -> delim fwsp SEMICOLON','delim',3,'p_delim','parser.py',30),
  ('delim -> COMMA','delim',1,'p_delim','parser.py',31),
  ('delim -> SEMICOLON','delim',1,'p_delim','parser.py',32),
  ('mailbox_or_url -> mailbox','mailbox_or_url',1,'p_expression_mailbox_or_url','parser.py',35),
  ('mailbox_or_url -> url','mailbox_or_url',1,'p_expression_mailbox_or_url','parser.py',36),
  ('url -> ofwsp URL ofwsp','url',3,'p_expression_url','parser.py',40),
  ('mailbox -> addr_spec','mailbox',1,'p_expression_mailbox','parser.py',44),
  ('mailbox -> angle_addr','mailbox',1,'p_expression_mailbox','parser.py',45),
  ('mailbox -> name_addr','mailbox',1,'p_expression_mailbox','parser.py',46),
  ('name_addr -> ofwsp phrase angle_addr','name_addr',3,'p_expression_name_addr','parser.py',50),
  ('angle_addr -> ofwsp LANGLE addr_spec RANGLE ofwsp','angle_addr',5,'p_expression_angle_addr','parser.py',54),
  ('addr_spec -> ofwsp local_part AT domain ofwsp','addr_spec',5,'p_expression_addr_spec','parser.py',58),
  ('local_part -> DOT_ATOM','local_part',1,'p_expression_local_part','parser.py',62),
  ('local_part -> ATOM','local_part',1,'p_expression_local_part','parser.py',63),
  ('local_part -> quoted_string','local_part',1,'p_expression_local_part','parser.py',64),
  ('domain -> DOT_ATOM','domain',1,'p_expression_domain','parser.py',68),
  ('domain -> ATOM','domain',1,'p_expression_domain','parser.py',69),
  ('domain -> domain_literal','domain',1,'p_expression_domain','parser.py',70),
  ('quoted_string -> DQUOTE quoted_string_text DQUOTE','quoted_string',3,'p_expression_quoted_string','parser.py',74),
  ('quoted_string -> DQUOTE DQUOTE','quoted_string',2,'p_expression_quoted_string','parser.py',75),
  ('quoted_string_text -> quoted_string_text QTEXT','quoted_string_text',2,'p_expression_quoted_string_text','parser.py',82),
  ('quoted_string_text -> quoted_string_text QPAIR','quoted_string_text',2,'p_expression_quoted_string_text','parser.py',83),
  ('quoted_string_text -> quoted_string_text fwsp','quoted_string_text',2,'p_expression_quoted_string_text','parser.py',84),
  ('quoted_string_text -> QTEXT','quoted_string_text',1,'p_expression_quoted_string_text','parser.py',85),
  ('quoted_string_text -> QPAIR','quoted_string_text',1,'p_expression_quoted_string_text','parser.py',86),
  ('quoted_string_text -> fwsp','quoted_string_text',1,'p_expression_quoted_string_text','parser.py',87),
  ('domain_literal -> LBRACKET domain_literal_text RBRACKET','domain_literal',3,'p_expression_domain_literal','parser.py',91),
  ('domain_literal -> LBRACKET RBRACKET','domain_literal',2,'p_expression_domain_literal','parser.py',92),
  ('domain_literal_text -> domain_literal_text DTEXT','domain_literal_text',2,'p_expression_domain_literal_text','parser.py',99),
  ('domain_literal_text -> domain_literal_text fwsp','domain_literal_text',2,'p_expression_domain_literal_text','parser.py',100),
  ('domain_literal_text -> DTEXT','domain_literal_text',1,'p_expression_domain_literal_text','parser.py',101),
  ('domain_literal_text -> fwsp','domain_literal_text',1,'p_expression_domain_literal_text','parser.py',102),
  ('comment -> LPAREN comment_text RPAREN','comment',3,'p_expression_comment','parser.py',106),
  ('comment -> LPAREN RPAREN','comment',2,'p_expression_comment','parser.py',107),
  ('comment_text -> comment_text CTEXT','comment_text',2,'p_expression_comment_text','parser.py',111),
  ('comment_text -> comment_text fwsp','comment_text',2,'p_expression_comment_text','parser.py',112),
  ('comment_text -> CTEXT','comment_text',1,'p_expression_comment_text','parser.py',113),
  ('comment_text -> fwsp','comment_text',1,'p_expression_comment_text','parser.py',114),
  ('phrase -> phrase fwsp ATOM','phrase',3,'p_expression_phrase','parser.py',118),
  ('phrase -> phrase fwsp DOT_ATOM','phrase',3,'p_expression_phrase','parser.py',119),
  ('phrase -> phrase fwsp DOT','phrase',3,'p_expression_phrase','parser.py',120),
  ('phrase -> phrase fwsp quoted_string','phrase',3,'p_expression_phrase','parser.py',121),
  ('phrase -> phrase ATOM','phrase',2,'p_expression_phrase','parser.py',122),
  ('phrase -> phrase DOT_ATOM','phrase',2,'p_expression_phrase','parser.py',123),
  ('phrase -> phrase DOT','phrase',2,'p_expression_phrase','parser.py',124),
  ('phrase -> phrase quoted_string','phrase',2,'p_expression_phrase','parser.py',125),
  ('phrase -> ATOM','phrase',1,'p_expression_phrase','parser.py',126),
  ('phrase -> DOT_ATOM','phrase',1,'p_expression_phrase','parser.py',127),
  ('phrase -> DOT','phrase',1,'p_expression_phrase','parser.py',128),
  ('phrase -> quoted_string','phrase',1,'p_expression_phrase','parser.py',129),
  ('ofwsp -> fwsp comment fwsp','ofwsp',3,'p_expression_ofwsp','parser.py',138),
  ('ofwsp -> fwsp comment','ofwsp',2,'p_expression_ofwsp','parser.py',139),
  ('ofwsp -> comment fwsp','ofwsp',2,'p_expression_ofwsp','parser.py',140),
  ('ofwsp -> comment','ofwsp',1,'p_expression_ofwsp','parser.py',141),
  ('ofwsp -> fwsp','ofwsp',1,'p_expression_ofwsp','parser.py',142),
  ('ofwsp -> <empty>','ofwsp',0,'p_expression_ofwsp','parser.py',143),
  ('fwsp -> FWSP','fwsp',1,'p_expression_fwsp','parser.py',147),
]
