<map version="freeplane 1.5.9">
<!--To view this file, download free mind mapping software Freeplane from http://freeplane.sourceforge.net -->
<node TEXT="Place" FOLDED="false" ID="ID_676249628" CREATED="1512859596772" MODIFIED="1512859630020" LINK="Footsteps.mm" STYLE="oval">
<font SIZE="18"/>
<hook NAME="MapStyle" zoom="1.5">
    <properties fit_to_viewport="false;"/>

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node" STYLE="oval" UNIFORM_SHAPE="true" VGAP_QUANTITY="24.0 pt">
<font SIZE="24"/>
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="default" COLOR="#000000" STYLE="fork">
<font NAME="SansSerif" SIZE="10" BOLD="false" ITALIC="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details"/>
<stylenode LOCALIZED_TEXT="defaultstyle.attributes">
<font SIZE="9"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.note" COLOR="#000000" BACKGROUND_COLOR="#ffffff" TEXT_ALIGN="LEFT"/>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
<cloud COLOR="#f0f0f0" SHAPE="ROUND_RECT"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="styles.topic" COLOR="#18898b" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subtopic" COLOR="#cc3300" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subsubtopic" COLOR="#669900">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.important">
<icon BUILTIN="yes"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="AutomaticLayout.level.root" COLOR="#000000" STYLE="oval" SHAPE_HORIZONTAL_MARGIN="10.0 pt" SHAPE_VERTICAL_MARGIN="10.0 pt">
<font SIZE="18"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,1" COLOR="#0033ff">
<font SIZE="16"/>
<edge COLOR="#ff0000"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,2" COLOR="#00b439">
<font SIZE="14"/>
<edge COLOR="#0000ff"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,3" COLOR="#990000">
<font SIZE="12"/>
<edge COLOR="#00ff00"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,4" COLOR="#111111">
<font SIZE="10"/>
<edge COLOR="#ff00ff"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,5">
<edge COLOR="#00ffff"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,6">
<edge COLOR="#7c0000"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,7">
<edge COLOR="#00007c"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,8">
<edge COLOR="#007c00"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,9">
<edge COLOR="#7c007c"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,10">
<edge COLOR="#007c7c"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,11">
<edge COLOR="#7c7c00"/>
</stylenode>
</stylenode>
</stylenode>
</map_styles>
</hook>
<hook NAME="AutomaticEdgeColor" COUNTER="2" RULE="ON_BRANCH_CREATION"/>
<node TEXT="Properties" POSITION="left" ID="ID_1630667893" CREATED="1512860319781" MODIFIED="1512860323489">
<edge COLOR="#ff0000"/>
<node TEXT="ID" ID="ID_1079768750" CREATED="1512860375674" MODIFIED="1512860377366"/>
<node TEXT="Type" ID="ID_207173553" CREATED="1512860378014" MODIFIED="1512860379054"/>
<node TEXT="Description" ID="ID_741613693" CREATED="1512860380946" MODIFIED="1512860384944"/>
<node TEXT="Name" ID="ID_557646029" CREATED="1512860386107" MODIFIED="1512860387428"/>
<node TEXT="CanHaveBuildings" ID="ID_308470525" CREATED="1512860481096" MODIFIED="1512860486035"/>
</node>
<node TEXT="Methods" POSITION="left" ID="ID_1154522179" CREATED="1512858909783" MODIFIED="1512858914852">
<edge COLOR="#00ffff"/>
<node TEXT="Getters" ID="ID_293249093" CREATED="1512858949391" MODIFIED="1512858953611"/>
<node TEXT="Setters" ID="ID_1263773414" CREATED="1512858953971" MODIFIED="1512858956340"/>
</node>
<node TEXT="SubClasses" POSITION="right" ID="ID_1767509206" CREATED="1512860328359" MODIFIED="1512860331743">
<edge COLOR="#0000ff"/>
<node TEXT="Town" ID="ID_862736062" CREATED="1512860344472" MODIFIED="1512860345612">
<node TEXT="Properties" ID="ID_998689502" CREATED="1512860422720" MODIFIED="1512860430947">
<node TEXT="CanHaveBuildingds = True" ID="ID_1563043496" CREATED="1512860525894" MODIFIED="1512860534635"/>
</node>
<node TEXT="Methods" ID="ID_536882613" CREATED="1512860431339" MODIFIED="1512860433373"/>
</node>
<node TEXT="Dungeon" ID="ID_1350694037" CREATED="1512860346159" MODIFIED="1512860348036">
<node TEXT="Properties" ID="ID_1711233352" CREATED="1512860422720" MODIFIED="1512860430947">
<node TEXT="CanHaveBuildingds = False" ID="ID_1785180980" CREATED="1512860525894" MODIFIED="1512860551137"/>
</node>
</node>
<node TEXT="Mountain" ID="ID_1942467817" CREATED="1512860350045" MODIFIED="1512860351936">
<node TEXT="Properties" ID="ID_719965242" CREATED="1512860422720" MODIFIED="1512860430947">
<node TEXT="CanHaveBuildingds = Yes" ID="ID_1881182174" CREATED="1512860525894" MODIFIED="1512860596469"/>
</node>
</node>
<node TEXT="Forest" ID="ID_944658074" CREATED="1512860352672" MODIFIED="1512860354056">
<node TEXT="Properties" ID="ID_864324629" CREATED="1512860422720" MODIFIED="1512860430947">
<node TEXT="CanHaveBuildingds = Yes" ID="ID_868244348" CREATED="1512860525894" MODIFIED="1512860602030"/>
</node>
</node>
<node TEXT="Building" ID="ID_1508603336" CREATED="1512860640764" MODIFIED="1512860643082">
<node TEXT="WeaponShop" ID="ID_1360441853" CREATED="1512860656642" MODIFIED="1512860666958"/>
<node TEXT="ArmourShop" ID="ID_978710086" CREATED="1512860667297" MODIFIED="1512860672179"/>
<node TEXT="Inn" ID="ID_1301130057" CREATED="1512860672817" MODIFIED="1512860673737"/>
<node TEXT="Restaraunt" ID="ID_128364882" CREATED="1512860674001" MODIFIED="1512860678230"/>
<node TEXT="UrgentCare" ID="ID_1213417189" CREATED="1512860678734" MODIFIED="1512860683034"/>
<node TEXT="Harbor" ID="ID_675111083" CREATED="1512860698906" MODIFIED="1512860701076"/>
<node TEXT="Stable" ID="ID_740971663" CREATED="1512860702706" MODIFIED="1512860703947"/>
</node>
</node>
</node>
</map>
