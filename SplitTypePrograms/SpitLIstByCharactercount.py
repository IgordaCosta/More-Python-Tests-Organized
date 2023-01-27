import pprint

import base93Characterconversion

stringUsed = '1588315820312515890404296875158770566406251587705664062515877056640625158340185546875159267666015625158340185546875159235605468751592356054687515922249023437516080917968751592224902343751608091796875160809179687516124382812516124382812516027790039062516027790039062516027790039062516002248046875160528105468751600224804687516047722656251604772265625160492402343751615368945312516049240234375161536894531251615368945312516169345703125162027021484375161693457031251617452636718751617452636718751615587011718751616509667968751615587011718751616146093751616146093751615644042968751615644042968751612337792968751612337792968751612337792968751612282031251612318554687516112976562516115899414062516115899414062516131469726562516148407226562516131469726562516137702148437516137702148437516162271484375162239472656251616227148437516223947265625162239472656251622672753906251631697558593751622672753906251631697558593751631697558593751636979980468751637309765625163628632812516363064453125163630644531251635529394531251635529394531251631001269531251631581152343751631581152343751632121679687516336360351562516273911132812516273911132812516273911132812516267953125162679531251622012516220125162201251621870996093751621870996093751618721289062516187212890625161872128906251619204785156251619340332031251618036328125161911259765625161911259765625161969042968751623259082031251619690429687516232590820312516232590820312516240472656251624047265625161910546875161910546875161910546875161971718751621089355468751616910546875161691054687516169105468751616662890625161666289062516141324218751614886132812516148861328125161489707031251616643261718751614897070312516166432617187516166432617187516163834960937516163834960937516152726562516152726562516152726562516135078125161350781251610339843751610377832031251610377832031251611873437516137234375161175615234375161372343751613723437516135538085937516137435546875161343339843751613433398437516134333984375161462978515625161590576171875161411093751615905761718751615905761718751616531640625161833095703125161653164062516177803710937516177803710937516172887695312516172887695312516141163085937516145986328125161459863281251617739355468751618550292968751617540234375161855029296875161855029296875161895976562516234401367187516189597656251623440136718751623440136718751622997167968751623333691406251618898730468751618898730468751618898730468751617066210937516170662109375161538320312516155245117187516155245117187516151252929687516161112304687516147389648437516161112304687516161112304687516167578125162410039062516167578125162410039062516241003906251627898828125163146074218751627898828125163146074218751631460742187516388166015625163990390625163476230468751634762304687516347623046875163511445312516426355468751634950292968751642635546875164263554687516422464843751646880664062516422464843751645555859375164555585937516450998046875164509980468751641975164197516419751640641796875164064179687516360278320312516360278320312516360278320312516353216796875163532167968751634391796875163475078125163475078125163678271484375164334550781251636782714843751643345507812516433455078125164404921875164798046875164404921875164520195312516452019531251643401643401638361132812516383611328125163836113281251639615234375163961523437516369887695312516369887695312516369887695312516366874023437516367530273437516332360351562516332360351562516332360351562516334740234375163423945312516330612304687516330612304687516330612304687516322793945312516356055664062516322793945312516356055664062516356055664062516364350585937516393287109375163643505859375163932871093751639328710937516413214843751643310937516413214843751643310937516433109375164420371093751644316015625163854863281251638548632812516385486328125163615644531251636156445312516294417968751629441796875162944179687516284057617187516310534179687516284057617187516304216796875163042167968751629261035156251629305273437516260294921875162602949218751626029492187516263635742187516316366210937516263635742187516316366210937516316366210937516338477539062516391162109375163384775390625163911621093751639116210937516396365234375164540742187516396365234375164540742187516454074218751647203125165068476562516472031251650684765625165068476562516607232421875166590859375166009453125166590859375166590859375166528593751666066992187516652347656251666066992187516660669921875166625976562516669722656251661213476562516612134765625166121347656251658160351562516596626953125165816035156251658178515625165817851562516582730468751660195312516582730468751660195312516601953125166082516619496093751660825166194960937516619496093751664124609375166581660156251664124609375166581660156251665816601562516679769531251667976953125166278144531251662781445312516627814453125166257480468751662574804687516602626953125166114355468751661143554687516615199218751666642578125166151992187516666425781251666642578125166723105468751670977734375166663164062516709777343751670977734375167168964843751671689648437516671449218751667144921875166714492187516690302734375167140742187516690302734375167083281251670832812516706312516706312516682634765625166826347656251668263476562516670185546875166701855468751663390234375166339023437516633902343751662786718751663973046875166239394531251663973046875166397304687516643867187516740427734375166438671875167404277343751674042773437516749496093751674949609375167001464843751670014648437516700146484375166988769531251671457031251669625781251671457031251671457031251676398828125168053515625167639882812516772919921875167729199218751676531251676531251670868164062516713539062516713539062516703351562516711957031251669926562516705849609375167058496093751670857226562516716517578125167037089843751670370898437516703708984375167067167968751673469335937516702798828125167346933593751673469335937516735369140625167354296875167321308593751673213085937516732130859375166786425781251667864257812516652097656251665462516654625166626367187516719316406251666263671875167193164062516719316406251672750390625167275039062516690638671875166906386718751669063867187516687287109375167403671875166872871093751674036718751674036718751674446093751678964062516743410156251678964062516789640625168140605468751683818945312516814060546875168360039062516836003906251684005664062516840056640625167487851562516748785156251674878515625167327187516734353515625167270058593751673347460937516733474609375167396503906251673965039062516726548828125167265488281251672654882812516728716796875167287167968751670128320312516701283203125167012832031251670916992187516732476562516709169921875167278554687516727855468751672356445312516723564453125167108925781251671089257812516710892578125166968554687516696855468751665408984375166540898437516654089843751665448242187516661333984375166544824218751665835546875166583554687516640115234375166401152343751656445507812516564455078125165644550781251656428320312516564283203125165440507812516556792968751655679296875165599433593751657356640625165599433593751656282812516562828125165671835937516613363281251656718359375166133632812516613363281251665401562516730755859375166540156251673075585937516730755859375167316113281251673161132812516697212890625166972128906251669721289062516706945312516800515625167069453125168005156251680051562516834111328125168569121093751683411132812516853707031251685370703125168286542968751682865429687516742570312516742570312516742570312516750513671875167781152343751675051367187516778115234375167781152343751676350390625167651406251675904492187516759044921875167590449218751675477539062516759302734375167512734375167593027343751675930273437516776128906251677612890625167494863281251674948632812516749486328125167362578125167362578125167223984375167223984375167223984375167226699218751672960351562516672291015625166722910156251667229101562516670662109375166801718751667003515625166801718751668017187516677287109375166902324218751667474023437516690232421875166902324218751669051171875167098125166905117187516709812516709812516708208984375167088164062516682800781251668280078125166828007812516676908203125166884101562516676908203125166884101562516688410156251668608984375166860898437516670062516685634765625166856347656251668513085937516692699218751668513085937516692257812516692257812516693783203125166937832031251657233789062516572337890625165723378906251656923242187516569232421875165393242187516539324218751653932421875165437792968751656069921875165437792968751656069921875165606992187516560388671875165603886718751655357031251655754101562516557541015625165514160156251655141601562516516304687516516304687516516304687516494054687516494054687516414972656251643289648437516432896484375164497343751647237109375164497343751646712304687516467123046875164796171875164796171875164458691406251644586914062516445869140625164351777343751643517773437516400511718751640051171875164005117187516386111328125163869453125163849453125163869453125163869453125163804716796875163865644531251637189941406251637189941406251637189941406251637877929687516412208984375163787792968751641096875164109687516414857421875164148574218751638132812516381328125163813281251638183593751638183593751630334863281251630334863281251630334863281251629960546875162996054687516290274414062516293327148437516293327148437516300653320312516333140625163006533203125163331406251633314062516344757812516388708984375163447578125163864843751638648437516400037109375164399531251640003710937516439953125164399531251646244140625164718632812516453058593751645305859375164530585937516450304687516450304687516442556640625164444570312516444457031251643799804687516457033203125164379980468751644718751644718751644444531251644581835937516402796875164027968751640279687516397632812516397632812516367965820312516392472656251639247265625164233751649002343751642337516490023437516490023437516479451171875164800566406251645298046875164800566406251648005664062516507011718751660155468751650701171875166015546875166015546875165931699218751659316992187516489060546875164914667968751649146679687516472623046875165208476562516472623046875165208476562516520847656251651413476562516514134765625164794238281251648195703125164819570312516519976562516530675781251651997656251652009765625165200976562516504976562516504976562516475974609375164759746093751647597460937516474375165098632812516474375165098632812516509863281251651081835937516543910156251651081835937516543910156251654391015625165477597656251657630273437516547759765625165763027343751657630273437516572873046875165913515625165697949218751659135156251659135156251661721289062516628955078125166120976562516612097656251661209765625166108535156251663252343751661085351562516632523437516632523437516640228515625166402285156251658654296875165865429687516586542968751657665039062516591761718751657665039062516591761718751659176171875165925917968751659259179687516563464843751656346484375165634648437516571402343751706287304687516571402343751706287304687517062873046875173302968751738126367187517330296875173812636718751738126367187517302498046875173176054687517275009765625173176054687517317605468751730118164062517314681640625172921406251729214062517292140625172941132812517358208984375172941132812517358208984375173582089843751746924414062517568056640625174692441406251756805664062517568056640625175729238281251757292382812517500925781251750092578125175009257812517469822265625174788554687517452496093751747885546875174788554687517500833984375175019882812517482507812517482507812517482507812517477435546875175014863281251746152734375174615273437517461527343751744175781251744642578125174405898437517442103515625174421035156251747639257812517543611328125174763925781251754361132812517543611328125175528867187517591166015625175528867187517555345703125175553457031251754086328125175424199218751753872265625175400273437517540027343751748600585937517486005859375174370332031251743703320312517437033203125174344531251747316796875174341640625174731679687517473167968751747683398437517509882812517476833984375175098828125175098828125175212890625176062988281251752128906251760391601562517603916015625176066347656251769183593751760116406251769183593751769183593751770511914062517743289062517705119140625177432890625177432890625177781679687517819566406251777816796875177824941406251778249414062517779369140625177793691406251772424218751773902929687517739029296875177357441406251773574414062517709324218751772484960937517724849609375177197324218751772025390625177075507812517707550781251770755078125176892246093751768922460937517523386718751752338671875175233867187517531097656251753109765625174861562517486156251748615625174450761718751748998437517445076171875174899843751748998437517493292968751750207812517481476562517481476562517481476562517478880859375174958300781251747152148437517495830078125174958300781251749835351562517498353515625174683632812517489992187517489992187517497273437517531037109375174840527343751748405273437517484052734375174898242187517555470703125174898242187517548929687517548929687517569355468751758505468751756935546875175793300781251757933007812517584466796875177745761718751758446679687517774576171875177745761718751776888085937517768880859375177532460937517763757812517763757812517741023437517796796875177399648437517796796875177967968751781154492187517843404296875178115449218751783371484375178337148437517806037109375178060371093751779092578125177983242187517798324218751779018751785679101562517790187517856791015625178567910156251786267968751787272460937517861927734375178619277343751786192773437517832060546875178320605468751780875781251781340429687517813404296875178134042968751781628515625177973476562517797347656251779734765625177900312517790031251777543751778707226562517787072265625177875078125177875078125177381601562517738160156251773816015625177361601562517744273437517731236328125177442734375177442734375177429023437517745443359375177307246093751773580859375177358085937517741888671875177631132812517741888671875177631132812517763113281251776479882812517769009765625177226093751772260937517722609375177241484375177241484375176493847656251764938476562517649384765625176144218751761442187517560960937517560960937517560960937517523125175231251732786132812517335294921875173352949218751732514648437517325146484375172507871093751725078710937517250787109375172373496093751726608984375172373496093751724854687517248546875172175292968751721752929687517202929687517202929687517202929687517208423828125172838593751720842382812517283859375172838593751729144335937517332923828125172914433593751732783398437517327833984375173384492187517427103515625173384492187517427103515625174271035156251741661523437517416615234375173885039062517388503906251738850390625173798320312517380437517370373046875173703730468751737037304687517345630859375173456308593751732132617187517328718751732871875173094062517309406251725516796875172688437517268843751727928125173129218751727928125173129218751731292187517302367187517351183593751730236718751735012890625173501289062517350287109375173505878906251734873632812517350587890625173505878906251735321093751735321093751733404101562517334041015625173340410156251732931054687517343730468751732807421875173437304687517343730468751734299804687517365025390625173429980468751736502539062517365025390625173944628906251739446289062517384156251738799804687517387998046875174028984375174141347656251738197851562517381978515625173819785156251737746093751737746093751734989257812517349892578125173498925781251732011718751732011718751728518554687517285185546875172851855468751730283593751732950585937517299021484375173295058593751732950585937517330279296875173559160156251733027929687517355916015625173559160156251735562517358460937517353298828125173543222656251735432226562517344373046875173528261718751734217578125173492792968751734927929687517342933593751734293359375173295781251733604687517336046875173739375174213046875173739375174213046875174213046875174301640625174455058593751743016406251744550585937517445505859375174540195312517454019531251744304687517443046875174430468751742159960937517421599609375174040839843751740408398437517404083984375174025078125174025078125173916191406251739320117187517393201171875174030546875174108593751739555078125173955507812517395550781251740049609375174268339843751740049609375174268339843751742683398437517452332031251745915820312517451351562517459158203125174591582031251746937304687517480919921875174693730468751747689257812517476892578125174714746093751747147460937517449351562517454404296875174544042968751746774218751746774218751745347070312517465152343751746515234375174652421875174896855468751746524218751748968554687517489685546875174956757812517506226562517495675781251750622656251750622656251768193751802264843751768193751798999609375179899960937518001970703125180543125179719179687517971917968751797191796875179793457031251799703906251797934570312517990945312517990945312517976292968751797629296875179530644531251795722070312517957220703125179556894531251795568945312517912417968751791241796875179124179687517900056640625179370937517899980468751793709375179370937517954529296875179806191406251795452929687517980619140625179806191406251797558593751797558593751795958789062517959587890625179595878906251794469335937517944693359375179446933593751794469335937517944693359375'

TimeBased = False
ListOfSlices = []
stepUsed = 150
perParStep = stepUsed
for i in range(0, len(stringUsed), stepUsed):

    sliceGotten = stringUsed[i:perParStep]

    OtherNumer = sliceGotten
    dataString = base93Characterconversion.base93Characterconversion(TimeBased=TimeBased, OtherNumer=OtherNumer)

    ListOfSlices.append(dataString)
    perParStep += stepUsed
    
pprint.pprint(ListOfSlices)



print(len(ListOfSlices))